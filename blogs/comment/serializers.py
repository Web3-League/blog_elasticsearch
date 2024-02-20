from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'  # Ou spécifiez les champs que vous souhaitez inclure dans votre sérialiseur
