from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from django.core.files.base import ContentFile
from django.http import FileResponse
from django.conf import settings
import os
import logging

from .models import EncryptedVideo
from .encryption_utils import encrypt_video, decrypt_video
from .kafka_producer import send_video_upload_message

logger = logging.getLogger(__name__)

class EncryptedUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        video_file = request.FILES.get('file')
        title = request.data.get('title', 'Untitled')

        if not video_file:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

        # Encrypt the file and save it
        encrypted_content = encrypt_video(video_file.read())
        encrypted_file = ContentFile(encrypted_content, name=video_file.name + '.enc')

        # Save encrypted file to DB
        encrypted_video = EncryptedVideo.objects.create(title=title, file=encrypted_file)

        # Send Kafka message
        send_video_upload_message(
            video_id=encrypted_video.id,
            filename=encrypted_video.file.name,
            title=encrypted_video.title
        )

        return Response({'message': 'Encrypted upload successful', 'id': encrypted_video.id})

    def get(self, request, *args, **kwargs):
        video_id = request.query_params.get('id')
        if not video_id:
            return Response({'error': 'Video ID required'}, status=400)

        try:
            video = EncryptedVideo.objects.get(id=video_id)
        except EncryptedVideo.DoesNotExist:
            return Response({'error': 'Video not found'}, status=404)

        # Read encrypted content from disk
        encrypted_path = video.file.path
        try:
            with open(encrypted_path, 'rb') as f:
                encrypted_content = f.read()
        except Exception as e:
            return Response({'error': f'Error reading file: {str(e)}'}, status=500)

        try:
            decrypted_content = decrypt_video(encrypted_content)
        except Exception as e:
            logger.error(f"Decryption failed: {str(e)}")
            return Response({'error': f'Decryption failed: {str(e)}'}, status=400)

        # Basic MP4 header check (optional, improves safety)
        if not decrypted_content.startswith(b'\x00\x00\x00') and b'ftyp' not in decrypted_content[:32]:
            return Response({'error': 'Decrypted content is not a valid MP4 file'}, status=400)

        # Serve file directly (no saving to disk)
        return FileResponse(
    ContentFile(decrypted_content),
    as_attachment=False,  # ✅ Stream inline in browser
    filename=f"{video.title}_decrypted.mp4",
    content_type='video/mp4'
)
    
from django.http import StreamingHttpResponse, HttpResponse
from django.shortcuts import get_object_or_404
import re
import mimetypes

RANGE_HEADER_PATTERN = re.compile(r'bytes=(\d+)-(\d*)')

def stream_video(request):
    video_id = request.GET.get('id')
    if not video_id:
        return HttpResponse("Video ID is required", status=400)

    video = get_object_or_404(EncryptedVideo, id=video_id)

    try:
        with open(video.file.path, 'rb') as f:
            encrypted = f.read()
        decrypted = decrypt_video(encrypted)
    except Exception as e:
        return HttpResponse(f"Decryption error: {e}", status=500)

    range_header = request.META.get('HTTP_RANGE', '')
    match = RANGE_HEADER_PATTERN.match(range_header)

    content_type, _ = mimetypes.guess_type(video.file.name)
    content_type = content_type or 'video/mp4'

    if match:
        start = int(match.group(1))
        end = int(match.group(2)) if match.group(2) else len(decrypted) - 1
        chunk = decrypted[start:end+1]
        response = StreamingHttpResponse(iter([chunk]), status=206, content_type=content_type)
        response['Content-Range'] = f'bytes {start}-{end}/{len(decrypted)}'
        response['Content-Length'] = str(end - start + 1)
        response['Accept-Ranges'] = 'bytes'
    else:
        response = StreamingHttpResponse(iter([decrypted]), content_type=content_type)
        response['Content-Length'] = str(len(decrypted))
        response['Accept-Ranges'] = 'bytes'

    return response
