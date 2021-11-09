from django.db import models
from django.db.models.fields import CharField
from django import forms


# Create your models here.




class Category(models.Model):
    def __str__(self):
        return self.category
    category = CharField(max_length=200)

class Cast(models.Model):
    def __str__(self):
        return self.actor_actress
    actor_actress = models.CharField(max_length=200)


class Movie(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    file_url = models.CharField(max_length=20, null=True)
    actors = models.ManyToManyField(Cast)
    categories = models.ManyToManyField(Category)
    #image = models.ImageField(upload_to="images", null=True)
    publication_date = models.DateTimeField('Date Published')



class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    movie = models.OneToOneField(
        Movie,
        on_delete=models.CASCADE,
        
    )



