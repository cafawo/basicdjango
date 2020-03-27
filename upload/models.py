from django.db import models

# Create your models here.

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y')
    timestamp = models.DateTimeField(auto_now_add=True)
    file_name = models.CharField('File name', max_length=200)  # <-- OPTIONAL
    file_type = models.CharField('File type', max_length=10)  # <-- OPTIONAL
    file_size = models.FloatField('File size (kb)')  # <-- OPTIONAL