from django.db import models
from django.db.models import (
    CharField,
    TextField,
    ForeignKey,
    DateTimeField,
    CASCADE,
    SET_NULL,
    EmailField
)


class Race(models.Model):
    name = CharField(max_length=255, unique=True)
    description = TextField(blank=True)


class Skill(models.Model):
    name = CharField(max_length=255, unique=True)
    bonus = CharField(max_length=255)
    race = ForeignKey(Race, on_delete=CASCADE, related_name="skills")

    def __repr__(self) -> str:
        return f"{self.name}, bonus: {self.bonus}, race: {self.race}"


class Guild(models.Model):
    name = CharField(max_length=255, unique=True)
    description = TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Player(models.Model):
    nickname = CharField(max_length=255, unique=True)
    email = EmailField(max_length=255)
    bio = CharField(max_length=255)
    race = ForeignKey(Race, on_delete=CASCADE, related_name="players")
    guild = ForeignKey(Guild, on_delete=SET_NULL, null=True)
    created_at = DateTimeField(auto_now_add=True)
