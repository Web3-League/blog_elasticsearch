# post/views.py

from django.http import JsonResponse, HttpResponse
from blog.models import BlogPost
from comment.models import Comment
from blog.serializers import BlogPostSerializer
from comment.serializers import CommentSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 

@api_view(['GET'])
def fetch_blog_post(request, post_id):
    try:
        blog_post = BlogPost.objects.get(pk=post_id)
    except BlogPost.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogPostSerializer(blog_post)
        request.session['fetched_post'] = True  # Adjust the flag for a single post
        return JsonResponse(serializer.data)

@api_view(['POST'])
def submit_comment(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        
        # Ensure the blog post ID is provided in the request
        blog_post_id = data.get('post')
        if not blog_post_id:
            return HttpResponse("Missing blog post ID.", status=status.HTTP_400_BAD_REQUEST)
        
        # Check if the specified blog post exists
        try:
            data['post'] = BlogPost.objects.get(pk=blog_post_id)
        except BlogPost.DoesNotExist:
            return HttpResponse("Blog post not found.", status=status.HTTP_404_NOT_FOUND)
        
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)