from django.db import models
from django.db.models import SET_NULL


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, null=True, on_delete=SET_NULL)


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=SET_NULL, null=True)
    guild = models.ForeignKey(Guild, on_delete=SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now=True)
