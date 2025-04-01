from tkinter.constants import CASCADE

from django.db import models
from django.db.models import ForeignKey
from django.db.models.fields import CharField, TextField, EmailField, DateField


class Race(models.Model):
    name = CharField(max_length=255, unique=True)
    description = TextField(blank=True)


class Skill(models.Model):
    name = CharField(max_length=255, unique=True)
    bonus = CharField(max_length=255)
    race = ForeignKey(Race, on_delete=CASCADE)


class Guild(models.Model):
    name = CharField(max_length=255, unique=True)
    description = TextField(null=True)


class Player(models.Model):
    nickname = CharField(max_length=255, unique=True)
    email = EmailField(max_length=255)
    bio = CharField(max_length=255)
    race = ForeignKey(Race, on_delete=CASCADE)
    guild = ForeignKey(Guild, on_delete=models.SET_NULL, null=True)
    created_at = DateField(auto_now_add=True)