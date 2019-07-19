from datetime import datetime

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Season(models.Model):
    year = models.IntegerField(verbose_name=_("Year"))

    @staticmethod
    def current_season():
        """"
        Calculate the current season.
        Season starts in August. Before that we show the previous season.
        """
        today = datetime.today()
        if today.month < 8:
            return today.year - 1
        else:
            return today.year

    def __str__(self):
        return f"{self.year} - {self.year+1}"


class Game(models.Model):
    gameweek = models.ForeignKey(
        "Gameweek",
        verbose_name=_("Game week"),
        on_delete=models.CASCADE,
        related_name="games",
    )
    home_team = models.ForeignKey(
        "Team",
        verbose_name=_("Home team"),
        on_delete=models.CASCADE,
        related_name="home_games",
    )
    away_team = models.ForeignKey(
        "Team",
        verbose_name=_("Away team"),
        on_delete=models.CASCADE,
        related_name="away_games",
    )
    goals_home = models.IntegerField(verbose_name=_("Goals home"))
    goals_away = models.IntegerField(verbose_name=_("Goals away"))
    result = models.CharField(max_length=2, verbose_name=_("Result"))

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"


class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    nick_name = models.CharField(max_length=10, verbose_name=_("Nick name"))

    def __str__(self):
        return self.name


class Gameweek(models.Model):
    season = models.ForeignKey(
        Season,
        on_delete=models.CASCADE,
        related_name="gameweeks",
        verbose_name=_("Season"),
    )
    number = models.IntegerField(verbose_name=_("Gameweek number"))
    start_date = models.DateField(verbose_name=_("Start date"))
    end_date = models.DateField(verbose_name=_("End date"))
    deadline = models.DateField(verbose_name=_("Deadline"))

    def __str__(self):
        return f"Gameweek {self.number}"


class Prediction(models.Model):
    choices = [
        ("1", _("Home teams wins")),
        ("X", _("Tie")),
        ("2", _("Away team wins")),
    ]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="predictions",
        verbose_name=_("User"),
    )
    game = models.ForeignKey(
        "Game",
        on_delete=models.CASCADE,
        related_name="predictions",
        verbose_name=_("Game"),
    )
    value = models.CharField(max_length=2, verbose_name=_("Value"), choices=choices)

    def __str__(self):
        return f"{self.user}: {self.game}"
