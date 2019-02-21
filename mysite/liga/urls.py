from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('rosters', views.rosters, name='rosters'),
    path('rosters/<int:owner_id>', views.rosters, name='detail')
]
