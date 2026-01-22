from django.db import models
from django.db.models import ForeignKey


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = ForeignKey(Race, on_delete=models.CASCADE, related_name="players")
    guild = ForeignKey(
        Guild, on_delete=models.SET_NULL, null=True, related_name="players"
    )
    created_at = models.DateTimeField(auto_now_add=True)
