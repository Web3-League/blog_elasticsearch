
from django.urls import path
from . import views

urlpatterns = [
    path('fetch-blog-posts/<int:post_id>/', views.fetch_blog_post, name='fetch-blog-posts'),
    path('submit-comment/', views.submit_comment, name='submit-comment'),
]
