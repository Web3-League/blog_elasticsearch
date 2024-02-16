from rest_framework import generics
from .models import Categorie
from .serializers import serializers


class CategorieList(generics.ListAPIView):
    queryset = Categorie.objects.all()
    serializer_class = serializers


class CategorieDetail(generics.RetrieveAPIView):
    queryset = Categorie.objects.all()
    serializer_class = serializers

