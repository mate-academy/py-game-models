from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255, blank=True, null=True, default=None)
    race = models.ForeignKey(Race, related_name="skills", on_delete=models.CASCADE)  # Updated related_name


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True, default=None)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255, blank=True)
    race = models.ForeignKey(Race, related_name="players", on_delete=models.CASCADE)  # Updated related_name
    guild = models.ForeignKey(Guild, related_name="players", on_delete=models.SET_NULL, null=True, default=None)  # Updated related_name
    created_at = models.DateTimeField(auto_now_add=True)
