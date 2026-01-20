from django.db import models


class Race(models.Model):
    races = [
        ("Elf", "Elf"),
        ("Dwarf", "Dwarf"),
        ("Human", "Human"),
        ("Ork", "Ork")
    ]

    name = models.CharField(max_length=255, choices=races, unique=True)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race,
                             on_delete=models.CASCADE,
                             related_name="skills")


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255, blank=True, null=True)
    race = models.ForeignKey(Race,
                             on_delete=models.CASCADE,
                             related_name="player_races")
    guild = models.ForeignKey(Guild,
                              on_delete=models.SET_NULL,
                              null=True,
                              related_name="player_guilds")
    created_at = models.DateTimeField(auto_now_add=True)
