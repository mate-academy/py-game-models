from django.db import models
from django.db.models import CASCADE, SET_NULL


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=CASCADE, related_name="skills")


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=False)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=CASCADE, related_name="players")
    guild = models.ForeignKey(
        Guild,
        on_delete=SET_NULL,
        null=True,
        blank=True,
        related_name="players"
    )
    created_at = models.DateTimeField(auto_now_add=True)
