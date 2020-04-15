"""basicdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # <--NEW

admin.site.site_header = "BasicDjango Admin"  # <-- NEW
admin.site.site_title = "BasicDjango Admin Portal"  # <--NEW
admin.site.index_title = "Welcome to BasicDjango"  # <--NEW

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', include('form.urls')),  # <--NEW
    path('', include('form.urls')),  # <--NEW, in case you want to redirect to the form directly
    path('upload/', include('upload.urls')),
    path('report/', include('report_builder.urls'))  # <-- NEW (django-report-builder)
]


#%% NEW this is a short cut to serve (uploaded) media directly
# Background: Django does not serve MEDIA_ROOT by default. That would be dangerous in production environment.
from django.conf import settings  # <-- NEW
from django.conf.urls.static import static  # <-- NEW

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)