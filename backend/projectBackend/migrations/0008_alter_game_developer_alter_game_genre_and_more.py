# Generated by Django 4.0.2 on 2022-04-10 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectBackend', '0007_rename_games_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='developer',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='game',
            name='genre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='game',
            name='publisher',
            field=models.CharField(max_length=50),
        ),
    ]