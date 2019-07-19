from django.db import models

# Create your models here.
class Game(models.Model):
    gameweek = models.ForeignKey(
        'Gameweek',
        on_delete=models.CASCADE,
        related_name='games'
    )
    home_team = models.ForeignKey(
        'Team',
        on_delete=models.CASCADE,
        related_name='home_games'
    )
    away_team = models.ForeignKey(
        'Team',
        on_delete=models.CASCADE,
        related_name='away_games'
    )
    result = models.CharField(max_length=2)

    def __str__(self):
        return str(self.home_team)+' vs '+str(self.away_team)

class Team(models.Model):
    name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=10)
    points = models.IntegerField()
    wins = models.IntegerField()
    defeats = models.IntegerField()
    ties = models.IntegerField()
    goals_home = models.IntegerField()
    goals_away = models.IntegerField()

    def __str__(self):
        return self.name

class Gameweek(models.Model):
    week_number = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    deadline = models.DateField()

    def __str__(self):
        return 'Gameweek '+str(self.week_number)

class Usser(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    score =models.IntegerField()

    def __str__(self):
        return self.name

class Prediction(models.Model):
    user = models.ForeignKey(
        'Usser',
        on_delete=models.CASCADE,
        related_name='predictions'
    )
    game = models.ForeignKey(
        'Game',
        on_delete=models.CASCADE,
        related_name='predictions'
    )
    gameweek = models.ForeignKey(
        'Gameweek',
        on_delete=models.CASCADE,
        related_name='predictions'
    )
    value = models.CharField(max_length=2)

    def __str__(self):
        return str(self.user)+' : '+str(self.game)
