from django import forms
from .models import Movie


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Movie
        fields = ('name', "actor", "categories", 'image')