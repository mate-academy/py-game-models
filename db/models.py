from django.db import models
from django.db.models import CASCADE, SET_NULL, ForeignKey
from django.db.models.fields import (
    CharField,
    DateTimeField,
    EmailField,
    TextField,
)


class Race(models.Model):
    name = CharField(unique=True, max_length=255)
    description = TextField(blank=True)


class Skill(models.Model):
    name = CharField(unique=True, max_length=255)
    bonus = CharField(max_length=255)
    race = ForeignKey(Race, on_delete=CASCADE, related_name="skills")


class Guild(models.Model):
    name = CharField(unique=True, max_length=255)
    description = TextField(null=True)


class Player(models.Model):
    nickname = CharField(unique=True, max_length=255)
    email = EmailField(max_length=255)
    bio = CharField(max_length=255)
    race = ForeignKey(Race, on_delete=CASCADE, related_name="players")
    guild = ForeignKey(
        Guild, on_delete=SET_NULL, null=True, related_name="players"
    )
    created_at = DateTimeField(auto_now_add=True)
