from django.urls import path
from .views import add_comment, get_comments

urlpatterns = [
    path('add/<int:post_id>/', add_comment, name='add-comment'),
    path('list/<int:post_id>/', get_comments, name='get-comments'),
]
