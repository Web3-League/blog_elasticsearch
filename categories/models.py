from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    # Ajoutez d'autres champs au besoin

    def __str__(self):
        return self.nom
