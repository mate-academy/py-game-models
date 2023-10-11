from django.db import models
from django.db.models import CharField


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self) -> CharField:
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self) -> CharField:
        return self.name


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True, null=True)
    description = models.TextField(null=True)

    def __str__(self) -> CharField:
        return self.name


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.SET_NULL, null=True)
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> CharField:
        return self.nickname
    
