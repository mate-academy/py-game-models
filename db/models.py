from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField("Kind of bonus you can get", max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True, null=True)
    description = models.TextField(blank=True, null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField("Short description about user", max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE,
                             related_name="races")
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE, null=True,
                              related_name="guilds")
    created_at = models.DateTimeField(auto_now_add=True)
