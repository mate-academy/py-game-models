from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Skill(models.Model):
    name = models.CharField(max_length=255)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE,
                             related_name="skills")


class Guild(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default=None, null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    bio = models.CharField(max_length=255, default=None, null=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE,
                             related_name="players")
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL,
                              default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
