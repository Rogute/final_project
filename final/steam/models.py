from django.db import models

GAME_GENRE = (
    (1, "Action"),
    (2, "Adventure"),
    (3, "Casual"),
    (4, "Massively Multiplayer"),
    (5, "Racing"),
    (6, "RPG"),
    (7, "Simulation"),
    (8, "Sports"),
    (9, "Strategy")
)


class ListOfGames(models.Model):
    name = models.CharField(max_length=128, verbose_name="Name of game")
    link = models.CharField(
        max_length=256,
        verbose_name="Link from steam",
        help_text="https://store.steampowered.com/app/...")
    genre = models.IntegerField(choices=GAME_GENRE)

    def __str__(self):
        return self.name
