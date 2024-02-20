from django.urls import path
from .views import search_view   # Assurez-vous d'importer la vue de recherche depuis votre fichier views.py

urlpatterns = [
    path('find/<str:query>/', search_view,  name='search'),  # Ajoutez la route de recherche avec le chemin '/search/'

]
