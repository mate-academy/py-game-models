from django.db import models
from django.utils import timezone


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(
        "Race",
        on_delete=models.CASCADE,
        related_name="skills"
    )

    def __str__(self) -> str:
        return self.name


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return self.name


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=False)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(
        "Race",
        on_delete=models.CASCADE
    )
    guild = models.ForeignKey(
        "Guild",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="members"
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        editable=False
    )

    def __str__(self) -> str:
        return self.nickname
