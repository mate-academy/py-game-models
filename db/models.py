from django.db import models
from django.db.models import CharField, TextField, ForeignKey, DateTimeField, EmailField


class Race(models.Model):
    name = CharField(max_length=255, unique=True)
    description = TextField(blank=True)


class Guild(models.Model):
    name = CharField(max_length=255, unique=True)
    description = TextField(null=True)


class Skill(models.Model):
    name = CharField(max_length=255, unique=True)
    bonus = CharField(max_length=255)
    race = ForeignKey(Race, on_delete=models.DO_NOTHING, related_name="skills")


class Player(models.Model):
    nickname = CharField(max_length=255, unique=True)
    email = EmailField(max_length=255)
    bio = CharField(max_length=255)
    race = ForeignKey(Race, on_delete=models.DO_NOTHING, related_name="players")
    guild = ForeignKey(Guild, on_delete=models.DO_NOTHING, null=True, related_name="guilds")
    created_at = DateTimeField(auto_now=True)

