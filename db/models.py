from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(
        "Field describes what kind of bonus the player can get from it.",
        max_length=255
    )
    race = models.ForeignKey(
        Race,
        on_delete=models.SET_NULL,
        related_name="skill_set",
        null=True
    )


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(
        "Short description provided by a user about himself/herself.",
        max_length=255
    )
    race = models.ForeignKey(
        Race,
        on_delete=models.SET_NULL,
        related_name="player_races",
        null=True
    )
    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,
        related_name="guilds",
        null=True
    )
    created_at = models.DateTimeField(auto_now=True)
