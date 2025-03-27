from django.db import models


# Race model
class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# Skill model
class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.IntegerField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name='skills')

    def __str__(self):
        return self.name


# Guild model
class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


# Player model
class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nickname
