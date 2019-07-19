from django.contrib import admin

from ..users.models import User
from .models import Game, Gameweek, Prediction, Season, Team

# Register your models here.
admin.site.register([User, Team, Game, Gameweek, Prediction, Season])
