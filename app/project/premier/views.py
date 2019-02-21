from premier.models import Team, Game
from premier.serializers import TeamSerializer, GameSerializer
from rest_framework import generics

# Create your views here.
class TeamListCreate(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class GameListCreate(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer