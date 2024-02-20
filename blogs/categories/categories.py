from django.urls import path
from .views import CategorieList, CategorieDetail

urlpatterns = [
    path('categories/', CategorieList.as_view(), name='categorie-list'),
    path('categories/<int:pk>/', CategorieDetail.as_view(), name='categorie-detail'),
]
