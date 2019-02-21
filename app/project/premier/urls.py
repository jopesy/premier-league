from django.urls import path
from . import views

urlpatterns = [
    path('api/teams/', views.TeamListCreate.as_view()),
    path('api/games/', views.GameListCreate.as_view()),
]