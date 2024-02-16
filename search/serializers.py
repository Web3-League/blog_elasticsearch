from rest_framework import serializers

class RechercheSerializer(serializers.Serializer):
    mot_recherche = serializers.CharField()
