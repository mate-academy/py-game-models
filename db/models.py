from django.db import models


class Race(models.Model):

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)


class Skill(models.Model):

    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.OneToOneField(Race, on_delete=models.CASCADE)


class Guild(models.Model):

    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, null=True)


class Player(models.Model):

    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=False)
    bio = models.CharField(max_length=255)
    race = models.OneToOneField(Race, on_delete=models.CASCADE)
    guild = models.OneToOneField(Guild, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
