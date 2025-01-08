from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(
        "db.Race",
        on_delete=models.CASCADE,
        related_name="skill_set"
    )


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(
        "db.Race",
        on_delete=models.CASCADE,
        related_name="players_of_race"
    )
    guild = models.ForeignKey(
        "db.Guild",
        null=True,
        on_delete=models.SET_NULL,
        related_name="players_in_guild"
    )
    created_at = models.DateTimeField(auto_now_add=True)
