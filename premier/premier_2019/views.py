from .models import Team, Game, Prediction
from .serializers import TeamSerializer, GameSerializer, PredictionSerializer
from rest_framework import generics
from django.shortcuts import render

# Create your views here.
def IndexView(request):
    return render(request, 'premier/index.html', {})

class TeamListCreate(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class GameListCreate(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class PredictionListCreate(generics.ListCreateAPIView):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer