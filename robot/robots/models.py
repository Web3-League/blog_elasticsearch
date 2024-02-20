# models.py dans l'application robots
from django.db import models
# models.py dans votre application Elasticsearch
from elasticsearch_dsl import Document, Text, Keyword, Integer

class RobotDocument(Document):
    name = Text(fields={'keyword': Keyword()})
    description = Text()
    price = Integer()
    stock = Integer()

    class Index:
        name = 'search-robots_index'  # Nom de votre index Elasticsearch


class Robot(models.Model):
    """
    Modèle symbolique pour représenter les Robots dans l'interface d'administration Django.
    Ce modèle n'est pas destiné à être utilisé pour stocker des données réelles dans la base de données.
    """
    class Meta:
        verbose_name = "Robot"
        verbose_name_plural = "Robots"
        managed = False  # Aucune table ne sera créée dans la base de données pour ce modèle
