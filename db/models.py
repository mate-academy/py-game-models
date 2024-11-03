from django.db import models
from django.db.models import SET_NULL


class Race(models.Model):
    RACE_TYPE = (
        ("Elf", "Elf race"),
        ("Dwarf", "Dwarf race"),
        ("Human", "Human race"),
        ("Ork", "Ork race"),
    )
    name = models.CharField(max_length=255, unique=True, choices=RACE_TYPE)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race,
                             on_delete=models.CASCADE,
                             related_name="skill_set")


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race,
                             on_delete=models.CASCADE,
                             related_name="player_race")
    guild = models.ForeignKey(Guild,
                              on_delete=SET_NULL,
                              null=True,
                              related_name="player_guild")
    created_at = models.DateTimeField(auto_now_add=True)
