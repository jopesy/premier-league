from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView, name='index_view'),
    path('api/teams/', views.TeamListCreate.as_view(), name='team_list'),
    path('api/games/', views.GameListCreate.as_view(), name='game_list'),
    path('api/predictions/', views.PredictionListCreate.as_view(), name='prediction_list'),
]