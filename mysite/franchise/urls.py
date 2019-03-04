from django.urls import path

from . import views

app_name = 'franchise'
urlpatterns = [
    path('', views.franchise, name='index'),
    path('update/<str:position>', views.update, name='update'),
]
