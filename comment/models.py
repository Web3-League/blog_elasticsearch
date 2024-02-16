from django.db import models
from blog.models import BlogPost

  # Assurez-vous d'importer le modèle BlogPost si nécessaire

class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]

