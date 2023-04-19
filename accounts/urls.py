from django.contrib.auth import login, authenticate
from django.urls import path
from .views import register

urlpatterns = [
    path('register/', register, name='register'
),
]