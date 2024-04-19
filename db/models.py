import datetime

from django.db import models
from django.utils import timezone


class Race(models.Model):
    AVAILABLE_RACE = [
        ("Elf", "Elf race had been chosen"),
        ("Dwarf", "Dwarf race had been chosen"),
        ("Human", "Human race had been chosen"),
        ("Ork", "Ork race had been chosen")
    ]
    name = models.CharField(
        max_length=255,
        unique=True,
        choices=AVAILABLE_RACE,
    )
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE
    )


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="race_players"
    )
    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,
        related_name="guild_players",
        null=True
    )
    created_at = models.DateTimeField(
        default=timezone.now
    )