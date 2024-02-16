from django.urls import path
from django.conf import settings
from .views import upload_media, media_list
from django.conf.urls.static import static
from .views import ImageUpload
from rest_framework.routers import DefaultRouter
from .views import MediaDeleteAPIView

urlpatterns = [
    path('upload/', upload_media, name='media-upload'),
    path('list/', media_list, name='media-list'),
    path('uploading/', ImageUpload.as_view(), name='media-upload-api'),
]

# Serving static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serving media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

router = DefaultRouter()
router.register(r'media', MediaDeleteAPIView, basename='media-delete')