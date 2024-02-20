from django.urls import path
from .views import BlogPostListCreate, BlogPostRetrieveUpdateDestroy


urlpatterns = [
    path('blogposts/', BlogPostListCreate.as_view(), name='blogpost-list'),
    path('blogposts/<int:pk>/', BlogPostRetrieveUpdateDestroy.as_view(), name='blogpost-detail'),
]
