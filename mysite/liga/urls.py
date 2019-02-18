from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rosters', views.rosters, name='rosters'),
    path('captracker', views.captracker, name='captracker'),
    path('franchise', views.franchise, name='franchise'),
]
