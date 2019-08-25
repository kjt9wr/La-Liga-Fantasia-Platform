from django.urls import path

from . import views

app_name = 'available'
urlpatterns = [
    path('', views.available, name='index'),
]