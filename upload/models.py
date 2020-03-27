from django.db import models

# Create your models here.

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y')
    timestamp = models.DateTimeField(auto_now_add=True)