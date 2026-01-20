from django.db import models


MAX_LENGTH = 255


class Race(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, unique=True)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, unique=True)
    bonus = models.CharField(max_length=MAX_LENGTH)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)


class Guild(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, unique=True)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=MAX_LENGTH, unique=True)
    email = models.EmailField(max_length=MAX_LENGTH)
    bio = models.CharField(max_length=MAX_LENGTH)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
