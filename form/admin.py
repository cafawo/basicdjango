from django.contrib import admin

# Register your models here.
from .models import SomeModel  # <-- NEW

# the PostAdmin class is cosmetic (optional)
class SomeModelAdmin(admin.ModelAdmin):  # <-- NEW
    list_display = ('date_submitted', 'first_name', 'last_name', 'first_number','second_number')
    list_filter = ("last_name",)
    search_fields = ['first_name', 'last_name']
    list_per_page = 20

admin.site.register(SomeModel, SomeModelAdmin)  # <-- NEW