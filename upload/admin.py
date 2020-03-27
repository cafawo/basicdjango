from django.contrib import admin

# Register your models here.
from .models import Document  # <-- NEW

# the PostAdmin class is cosmetic (optional)
class DocumentAdmin(admin.ModelAdmin):  # <-- NEW
    list_display = ('timestamp', 'docfile', 'file_name', 'file_type', 'file_size')
    list_filter = ('timestamp',)
    search_fields = ['timestamp', 'docfile']

admin.site.register(Document, DocumentAdmin)  # <-- NEW