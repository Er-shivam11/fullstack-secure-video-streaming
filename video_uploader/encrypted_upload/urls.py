from django.urls import path
from .views import EncryptedUploadView,stream_video

urlpatterns = [
    path('upload/', EncryptedUploadView.as_view(), name='encrypted-upload'),
    path('stream/', stream_video, name='stream-video'),  # ✅ Add this
]
