# Generated by Django 4.0.2 on 2022-02-10 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListOfGames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name of game')),
                ('link', models.CharField(help_text='https://store.steampowered.com/app/...', max_length=256, verbose_name='Link from steam')),
                ('genre', models.IntegerField(choices=[(1, 'Action'), (2, 'Adventure'), (3, 'Casual'), (4, 'Massively Multiplayer'), (5, 'Racing'), (6, 'RPG'), (7, 'Simulation'), (8, 'Sports'), (9, 'Strategy')])),
            ],
        ),
    ]
