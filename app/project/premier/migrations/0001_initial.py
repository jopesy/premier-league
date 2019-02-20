# Generated by Django 2.1.7 on 2019-02-20 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Gameweek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('deadline', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=2)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='predictions', to='premier.Game')),
                ('gameweek', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='predictions', to='premier.Gameweek')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nick_name', models.CharField(max_length=10)),
                ('points', models.IntegerField()),
                ('wins', models.IntegerField()),
                ('defeats', models.IntegerField()),
                ('ties', models.IntegerField()),
                ('goals_home', models.IntegerField()),
                ('goals_away', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='prediction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='predictions', to='premier.Usser'),
        ),
        migrations.AddField(
            model_name='game',
            name='away_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_games', to='premier.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='gameweek',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='premier.Gameweek'),
        ),
        migrations.AddField(
            model_name='game',
            name='home_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_games', to='premier.Team'),
        ),
    ]
