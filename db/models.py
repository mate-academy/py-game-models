from django.db import models
from django.db.models import SET_NULL


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField("A description of the bonus",
                             max_length=255, blank=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE,
                             related_name="skills")


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField("Info by user about user",
                           max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE,
                             related_name="race_members")
    guild = models.ForeignKey(Guild, on_delete=SET_NULL, null=True,
                              related_name="guild_members")
    created_at = models.DateTimeField(auto_now_add=True)
