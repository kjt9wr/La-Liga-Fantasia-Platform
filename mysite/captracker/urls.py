from django.urls import path

from . import views

urlpatterns = [
    path('', views.captracker, name='captracker'),
]
