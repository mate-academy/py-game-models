from django.db import models
from django.db.models import ForeignKey
from django.utils import timezone


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(
        "this is a description of the bonus",
        max_length=255
    )
    race = ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="skill_races"
    )


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(
        "short description provided by a user about himself/herself.",
        max_length=255
    )
    race = ForeignKey(Race, on_delete=models.CASCADE, related_name="races")
    guild = ForeignKey(
        Guild, on_delete=models.SET_NULL,
        null=True,
        related_name="guilds"
    )
    created_at = models.DateTimeField(default=timezone.now)
