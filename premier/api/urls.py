from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView, name="index_view"),
    path("seasons/", views.SeasonListCreate.as_view(), name="season_list"),
    path("gameweeks/", views.GameweekListCreate.as_view(), name="gameweek_list"),
    path("teams/", views.TeamListCreate.as_view(), name="team_list"),
    path("games/", views.GameListCreate.as_view(), name="game_list"),
    path("predictions/", views.PredictionListCreate.as_view(), name="prediction_list"),
    path("users/", views.UserListCreate.as_view(), name="user_list"),
]
