# Quick and dirty Python|Django (for data scientists)

The idea here is to have a template like minimum working example for Django in order to quickly get going with a simple (prototype) front-end.

This project (so far) includes
* a simple input form (data input),
* a simple file upload form,
* a basic data model,
* admin site integration,
* basic CSS styling,
* basic computations and result output.

and should look like this:

![form](form.PNG)


## Requirements:
* Python 3+ environment (I use Conda) with Django 2.2+. If you use Conda, you can create the environment from django.yaml (included).
```
conda env create -f django.yaml
```


## Quick start:
1. Activate your django environment
```
conda activate django
```
2. Migrate data base (SQLite by default, see below how to use PostgreSQL). Hint: check out http://inloop.github.io/sqlite-viewer/ to see SQLite contents
```
python manage.py makemigrations form
python manage.py makemigrations upload
python manage.py migrate
```
3. Create superuser (you could skip this step)
```
python manage.py createsuperuser --username=admin --email=email@domain.com
```
4. Run server
```
python manage.py runserver
```
The console should show something like:
```
Watching for file changes with StatReloader
Performing system checks...
System check identified no issues (0 silenced).
January 06, 2020 - 13:28:11
Django version 2.2.5, using settings 'basicdjango.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
5. Try out the form and admin area (login with your superuser)
```
http://127.0.0.1:8000/form
http://127.0.0.1:8000/admin
```

# More fun with Django


## MTV (Model Template View) design priciple:
* Model: data access layer
* Template: presentation layer
* View: bridge between model and template


## Create NEW project
1. Open console at project location (new project folder will be created here)
2. Initiate the project
```
django-admin startproject basicdjango
```
This will create a project folder including manage.py, which is a wrapper for django admin commands specific to this project. Apps have to be intergated into:
* settings.py (holds secret key (!) ... do not version)
* urls.py (routing within project/site)


## Apps
Each project (e.g. basicdjango) can contain multiple apps (e.g. blog, store). In this example, "form" is an app.
```
python manage.py startapp form
```

### Forms
In this example we define a form class in ``form/forms.py``. More information at:
* https://docs.djangoproject.com/en/2.2/topics/forms/
* https://docs.djangoproject.com/en/2.2/ref/forms/fields/

In ``form/views.py`` we then render the form via 
```python
render(request, 'form.html', {'form': form})
```

### Templates
See https://djangobook.com/mdj2-django-templates/

Site templates, at their most basic, are HTML files that are displayed by your browser. Django’s approach to web design is simple—keep Django logic and code separate from design. It’s very important to understand that Django’s templates are not simply Python code embedded into HTML; it’s not actually possible to execute Python code in a Django template.

A template tag is surrounded by {% and %}. A template tag does something, e.g.:
* Display Logic. E.g. ``{% if %}...{% endif %}``
* Loop Control. E.g. ``{% for x in y %}...{% endfor %}``

A template variable is surrounded by {{ and }}. A template variable is something, e.g.:
* Simple Variable. E.g. ``{{ title }}``
* Object Attribute. E.g. ``{{ page.title }}``
* Dictionary Lookup. E.g. ``{{ dict.key }}``
* List Index. E.g. ``{{ list_items.0 }}``


## Migrate to PostgreSQL
Check this link if you want to use multiple DBs: https://docs.djangoproject.com/en/3.0/topics/db/multi-db/
Or this link for multiple Posgtres schemas: https://www.amvtek.com/blog/posts/2014/Jun/13/accessing-multiple-postgres-schemas-from-django/
1. Change DATABASES in basicdjango/settings.py:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'basicdjango',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```
2. Make sure the package ``psycopg2`` is installed in your (conda) environment
3. Migrate to the new database
```
python manage.py migrate 
```

## Fetch data using Django's SQL connection directly
```Python
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("""SELECT * FROM table""")
    result = cursor.fetchall()
print(result)

# When using pandas as pd this is even simpler:
result = pd.read_sql("""SELECT * FROM table""", connection)
print(result)
# Hint: when serving data as JSON from pandas, this might help:
result.to_dict('list')
```


## Migrate an app
1. Create migrations
```
python manage.py makemigrations form
```
2. Check SQL code (optional)
```
python manage.py sqlmigrate form 0001
```
3. Migrate
```
python manage.py migrate
```
The migrate command will only run migrations for apps in settings.py: INSTALLED_APPS.


## Admin site integration
1. Add the data model of our form to the admin site, in ``form/admin.py``:
```python
from django.contrib import admin

# Register your models here.
from .models import SomeModel  # <-- NEW
admin.site.register(SomeModel)  # <-- NEW
```
2. Try the admin functions: http://127.0.0.1:8000/admin


## Integrate existing data base (model)
It is possible to integrate Django into legacy databases. 
1. Set up database connection for Django to connect to existing database in ``settings.py`` file.
2. Auto-generate models from an existing database via inspectdb.
```
python manage.py inspectdb
```
2.1 You can save this as a file by using standard Unix output redirection.
```
python manage.py inspectdb > models.py
```
2.2 You can pass table names as an argument.
```
python manage.py inspectdb table1 table2
```
https://docs.djangoproject.com/en/3.0/ref/django-admin/#django-admin-inspectdb


## Test your site on a local network
Note that the default IP address, 127.0.0.1, is not accessible from other machines on your network. To make your development server viewable to other machines on the network, use its own IP address (e.g. 192.168.2.1) or 0.0.0.0.
1. Find your IP (e.g. ipconfig)
2. Add your ip to ``basicdjango/settings.py``, e.g.
```python
ALLOWED_HOSTS = ['192.168.2.1']
```
3. Run server
```
python manage.py runserver 0.0.0.0:8000
```
4. Access the form from another device: http://192.168.2.1.8:8000/form


## Test you site on https://www.pythonanywhere.com/
Pythonanywhere has a free tier hosting service for python applications (incl. django). A complete guide can be found here: https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/

There are only two changes you have to make to this project:
1. Adjust ``basicdjango.settings.py``
```python
DEBUG = False  # <- CHANGE
ALLOWED_HOSTS = ["myusername.pythonanywhere.com"]  # <- CHANGE
```
2. Get the required static files (CSS), i.e. open a console in the project dir and run
```
python manage.py collectstatic
```


# Further resources
* Very well written tutorial that covers all the basics: https://docs.djangoproject.com/en/3.0/intro/tutorial01/
* A nice blog project: https://djangocentral.com/building-a-blog-application-with-django/
* Integrating existing DBs: https://dev.to/idrisrampurawala/creating-django-models-of-an-existing-db-288m

