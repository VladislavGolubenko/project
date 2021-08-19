from django.urls import path
from django.contrib import admin
from .views import * # импорт экшенов

urlpatterns = [
    path('', index),
]
