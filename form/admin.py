from django.contrib import admin

# Register your models here.
from .models import SomeModel  # <-- NEW
admin.site.register(SomeModel)  # <-- NEW