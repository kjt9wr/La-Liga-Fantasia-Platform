from django.urls import path

from . import views

app_name = 'liga'
urlpatterns = [
    path('', views.index, name='index'),
    path('rosters/<int:owner_id>', views.rosters, name='rosters'),
    path('rosters/<int:owner_id>/update/', views.update, name='update'),
]
