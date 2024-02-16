from django.http import JsonResponse
from media.forms import MediaForm
from .models import Media
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from media.forms import MediaForm
from .models import Media

# Vue pour le téléchargement de médias
def upload_media(request):
    if request.method == 'POST':
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            media = form.save()
            return JsonResponse({'media_id': media.id})
    else:
        return JsonResponse({'error': 'Invalid request method'})

# APIView pour le téléchargement d'images
class ImageUpload(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        if 'image' in request.FILES:
            image_file = request.FILES['image']
            form = MediaForm({'file': image_file})
            if form.is_valid():
                media = form.save()
                return Response({'message': 'Image uploaded successfully.', 'media_id': media.id})
            else:
                return Response(form.errors, status=400)
        else:
            return Response({'error': 'No image file provided.'}, status=400)

def media_list(request):
    media = Media.objects.all()
    data = [{'id': m.id, 'title': m.title, 'file_url': m.file.url} for m in media]
    return JsonResponse(data, safe=False)

import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Media

class MediaDeleteAPIView(APIView):
    def delete(self, request, pk, format=None):
        try:
            media = Media.objects.get(pk=pk)
        except Media.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Delete the associated file if it exists
        if media.file:
            try:
                os.remove(media.file.path)
            except OSError:
                pass  # Ignore errors if file doesn't exist or cannot be deleted

        # Delete the Media object from the database
        media.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)





