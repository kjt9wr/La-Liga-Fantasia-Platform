from django.urls import path

from . import views

app_name = 'captracker'
urlpatterns = [
    path('', views.captracker, name='captracker'),
    path('trade/view/<tid>', views.viewTrade, name='viewTrade'),
    path('trade/add', views.addTrade, name='addTrade'),

]
