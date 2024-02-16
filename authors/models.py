from django.db import models


class Author(models.Model):
    nom = models.CharField(max_length=100)
    bio = models.TextField()
    # Ajoutez d'autres champs au besoin

    def __str__(self):
        return self.nom
