from django.db import models

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=200, unique=True)

class Contact(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=200)

class Article(models.Model):
    available = models.BooleanField(default=True)
    titel = models.CharField(max_length=200)
    picture = models.URLField()
    types = models.ManyToManyField(Type, related_name='article', blank=True)

class Booking(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    article = models.OneToOneField(Article, on_delete=models.CASCADE)