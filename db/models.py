from django.db import models
from django.db.models import ForeignKey


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = ForeignKey(Race, on_delete=models.CASCADE, related_name="skills")


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=False)
    bio = models.CharField(max_length=255, null=True, blank=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = ForeignKey(Guild,
                       on_delete=models.SET_NULL,
                       related_name="players",
                       null=True)
    created = models.DateTimeField(auto_now_add=True)
