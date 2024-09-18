from django.db import models
from django.db.models import CharField


class Race(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self) -> CharField:
        return self.name


class Skills(models.Model):
    name = models.CharField(max_length=255)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        related_name="skill_set",
        on_delete=models.CASCADE
    )

    def __str__(self) -> CharField:
        return self.name


class Guild(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> CharField:
        return self.name


class PlayerModel(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        related_name="players_race",
        on_delete=models.CASCADE)
    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="guild_members")
    created_at = models.DateField(
        auto_now_add=True
    )

    def __str__(self) -> CharField:
        return self.nickname
