import os
from django import forms
from .models import Media


# Define target directory where your Django project's static folder is located
target_directory = r'static\media'

# Define Django form for uploading media
class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['title', 'file']

    def save(self, commit=True):
        media = super().save(commit=False)
        if commit:
            media.save()

        return media
    
    def clean(self):
        file = self.file

        if file:
            # Define the target directory where you want to save the file
            target_directory = '/media/media/'

            # Save the file to the target directory
            file_path = os.path.join(target_directory, file.name)
            with open(file_path, 'wb') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

        return super().clean()