from django.db import models

# Create your models here.

class Museo(models.Model):
    museo = models.CharField(max_length=200)
    descripción = models.TextField()
    dirección = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to = "projects")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

