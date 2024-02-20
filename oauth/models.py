from django.db import models


from django.db import models
from django.contrib.auth.models import User

class OAuthClient(models.Model):
    client_id = models.CharField(max_length=255, unique=True)
    client_secret = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The owner of the client

    def __str__(self):
        return self.name

class AccessToken(models.Model):
    token = models.CharField(max_length=255, unique=True)
    client = models.ForeignKey(OAuthClient, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expires = models.DateTimeField()

    def __str__(self):
        return self.token

class RefreshToken(models.Model):
    token = models.CharField(max_length=255, unique=True)
    access_token = models.OneToOneField(AccessToken, on_delete=models.CASCADE)
    expires = models.DateTimeField()

    def __str__(self):
        return self.token
