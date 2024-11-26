from django.db import models


class Race(models.Model):
    RACE_TYPE = (
        ("ELF", "Elf"),
        ("DWARF", "Dwarf"),
        ("HUMAN", "Human"),
        ("ORK", "Ork")
    )
    name = models.CharField(unique=True, max_length=255, choices=RACE_TYPE)
    description = models.TextField(null=True, blank=True)


class Skill(models.Model):
    name = models.CharField(unique=True, max_length=255)
    bonus = models.CharField("description of the bonus", max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)


class Guild(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(null=True, blank=True)


class Player(models.Model):
    nickname = models.CharField(unique=True, max_length=255)
    email = models.EmailField(max_length=255)
    bio = models.CharField("short description provided by a user",
                           max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE,
                             related_name="player_race")
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL,
                              null=True,
                              related_name="guild_of_player")
    created_at = models.DateTimeField(auto_now=True)
