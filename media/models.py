from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from urllib.parse import urlparse
import os

class Media(models.Model):
    title = models.CharField(max_length=100)
    file = models.ImageField(upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=255, blank=True, null=True)


    def save(self, *args, **kwargs):
        # Call the super method to save the model
        super().save(*args, **kwargs)
        
        # Extract the URL path from the file field and set it to the path attribute
        file_url = urlparse(self.file.url).path
        self.path = file_url

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

@receiver(pre_delete, sender=Media)
def delete_media_file(sender, instance, **kwargs):
    # Delete the file associated with the Media instance
    if instance.file:
        file_path = instance.file.path
        if os.path.exists(file_path):
            os.remove(file_path)
