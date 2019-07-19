from django.contrib import admin
from .models import Usser, Team, Game, Gameweek, Prediction

# Register your models here.
admin.site.register([Usser, Team, Game, Gameweek, Prediction])