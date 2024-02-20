from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.response import Response



class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer



    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    

class BlogListDelete(generics.DestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

