from typing import ForwardRef

from django.db import models
from django.db.models import DO_NOTHING, CASCADE


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=CASCADE)


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True, )
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=CASCADE)
    guild = models.ForeignKey(Guild, on_delete=DO_NOTHING)
    created_at = models.DateTimeField(auto_now=True)
