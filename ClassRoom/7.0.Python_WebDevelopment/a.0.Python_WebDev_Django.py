# Python Django Example

# Installation
'''
pip install django
'''


# Create a Django Project and App
'''
django-admin startproject myproject
cd myproject
python manage.py startapp myapp
'''

# Define a Model
from django.db import models

class Greeting(models.Model):
    message = models.CharField(max_length=100)
    
# Create the View
from django.shortcuts import render
from .models import Greeting

def home(request):
    greeting = Greeting.objects.first()  # Assuming a greeting instance exists
    return render(request, 'home.html', {'greeting': greeting})


# Create the templates
# myapp/templates/myapp/
'''
<!-- myapp/templates/home.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Greeting Page</title>
    <link rel="stylesheet" type="text/css" href="{% static 'css/styles.css' %}">
</head>
<body>
    <h1>{{ greeting.message }}</h1>
    <script src="{% static 'js/script.js' %}"></script>
</body>
</html>

'''

# Static: css and javascript
# static/css styles.css static/js script.js
'''
/* myapp/static/styles.css */
body {
    font-family: Arial, sans-serif;
    text-align: center;
}
'''
'''
// myapp/static/script.js
console.log("Page loaded!");

'''

# Configure the urls
# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Include myapp urls
]

# myapp/urls.py (new file)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

# update the settings
INSTALLED_APPS = [
    # ...
    'myapp',
]

STATIC_URL = '/static/'

# Run migrations
'''
python manage.py makemigrations
python manage.py migrate
'''

# Run the server
# access via http://localhost:8000
'''
python manage.py runserver
'''

# Create the superuser
# access via http://localhost:8000/admin
'''
python manage.py createsuperuser
'''