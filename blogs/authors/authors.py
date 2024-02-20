from django.urls import path
from .views import AuthorList, AuthorBio

urlpatterns = [
    path('list/', AuthorList.as_view(), name='author-list'),
    path('getById/<int:pk>/', AuthorBio.as_view(), name='author-detail'),
]