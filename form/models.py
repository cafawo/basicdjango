"""Simple data model

# Ressources
https://docs.djangoproject.com/en/3.0/intro/tutorial02/
"""
from django.db import models

class SomeModel(models.Model):
    date_submitted = models.DateTimeField('Date submitted')
    first_name = models.CharField('First name', max_length=200)
    last_name = models.CharField('Last name', max_length=200)
    first_number = models.FloatField('First number')
    second_number = models.FloatField('Second number')
    
    class Meta:
        # This will help is to return the latest DB entry, e.g.
        # latest_submission = SomeModel.objects.latest()
        # latest_submission = SomeModel.objects.earliest()
        get_latest_by = 'date_submitted'