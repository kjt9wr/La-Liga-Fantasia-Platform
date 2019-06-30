from django.urls import path

from . import views

app_name = 'captracker'
urlpatterns = [
    path('', views.captracker, name='captracker'),
    path('trade/view/<tid>', views.view_trade, name='viewTrade'),
    path('trade/add', views.add_trade, name='addTrade'),
    path('trade/submitTrade', views.submit, name='submit'),

]
