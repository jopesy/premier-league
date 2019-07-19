from django.shortcuts import render
from rest_framework import generics

# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from ..common.models import Game, Gameweek, Prediction, Season, Team
from ..common.serializers import (
    GameSerializer,
    GameweekSerializer,
    PredictionSerializer,
    SeasonSerializer,
    TeamSerializer,
)
from ..users.models import User
from ..users.serializers import UserSerializer


def IndexView(request):
    return render(request, "premier/index.html", {})


class SeasonListCreate(generics.ListCreateAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    permission_classes = [IsAuthenticated]


class TeamListCreate(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]


class GameweekListCreate(generics.ListCreateAPIView):
    queryset = Gameweek.objects.all()
    serializer_class = GameweekSerializer
    permission_classes = [IsAuthenticated]


class GameListCreate(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]


class PredictionListCreate(generics.ListCreateAPIView):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer
    permission_classes = [IsAuthenticated]


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
