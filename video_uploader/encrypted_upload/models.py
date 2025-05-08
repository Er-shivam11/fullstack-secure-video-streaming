from django.db import models



class EncryptedVideo(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='encrypted_videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
