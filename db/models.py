from django.db import models
from django.db.models import CharField


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True,)
    description = models.TextField(blank=True)

    def __str__(self) -> CharField:
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="skills"
    )

    def __str__(self) -> str:
        return f"{self.name} ({self.race})"


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True,)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> CharField:
        return self.name


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True,)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="players"
    )
    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="players"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> CharField:
        return self.nickname
