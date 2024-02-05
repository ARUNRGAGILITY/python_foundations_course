# Python API Example with Flask

from flask import Flask, jsonify, request

app = Flask(__name__)

# Example data store
data = {
    "message": "Hello, World!"
}

@app.route('/message', methods=['GET'])
def get_message():
    """Endpoint to get the current message"""
    return jsonify(data)

@app.route('/message', methods=['PUT'])
def update_message():
    """Endpoint to update the message"""
    new_message = request.json.get('message')
    if new_message:
        data["message"] = new_message
        return jsonify(data), 200
    else:
        return jsonify({"error": "No message provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)

# Run the Flask application
# python app.py

# curl -X GET http://127.0.0.1:5000/message
# curl -X PUT http://127.0.0.1:5000/message -H "Content-Type: application/json" -d '{"message": "Hello, Flask!"}'



# Python REST API example with djangorestframework

# Install Django REST Framework
# pip install django djangorestframework

# Create a Django Project and App
'''
django-admin startproject myproject
cd myproject
django-admin startapp myapi
'''

# Define the Model
# myapi/models.py
from django.db import models

class Message(models.Model):
    content = models.CharField(max_length=256)

# Create a Serializer
# myapi/serializers.py
from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'content']

# Create a Viewset
# myapi/views.py
from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

# Configure urls.py
# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapi.urls')),  # Include myapi urls
]

# myapi/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet

router = DefaultRouter()
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# Configure Settings
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'myapi',
]

# Run migrations
'''
python manage.py makemigrations myapi
python manage.py migrate
'''
# Run the server
'''
python manage.py runserver
'''