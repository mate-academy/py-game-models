from django.db import models
from typing import Optional
from datetime import datetime


class Race(models.Model):
    name: str = models.CharField(max_length=255, unique=True)
    description: Optional[str] = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Skill(models.Model):
    name: str = models.CharField(max_length=255, unique=True)
    bonus: str = models.CharField(max_length=255)
    race: "Race" = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="skills"
    )

    def __str__(self) -> str:
        return self.name


class Guild(models.Model):
    name: str = models.CharField(max_length=255, unique=True)
    description: Optional[str] = models.TextField(null=True)

    def __str__(self) -> str:
        return self.name


class Player(models.Model):
    nickname: str = models.CharField(max_length=255, unique=True)
    email: str = models.EmailField(max_length=255)
    bio: str = models.CharField(max_length=255)
    race: "Race" = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="players"
    )
    guild: Optional["Guild"] = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="members"
    )
    created_at: datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nickname
