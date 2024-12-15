from django.db import models
from django.db.models import DateTimeField


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        related_name="skill_set",
        on_delete=models.CASCADE
    )


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        related_name="race_set",
        on_delete=models.CASCADE
    )
    guild = models.ForeignKey(
        Guild,
        related_name="guild_set",
        null=True,
        on_delete=models.SET_NULL
    )
    created_at = DateTimeField(auto_now_add=True)
