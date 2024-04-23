from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(to=Race, on_delete=models.CASCADE)

class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)


class Players(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(to=Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(to=Guild, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)