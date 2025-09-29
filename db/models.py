from django.db import models
from django.utils import timezone


class Race(models.Model):
    name: str = models.CharField(max_length=255, unique=True)
    description: str = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Skill(models.Model):
    name: str = models.CharField(max_length=255, unique=True)
    bonus: str = models.CharField(max_length=255)
    race: Race = models.ForeignKey(
        Race, on_delete=models.CASCADE, related_name="skills"
    )

    def __str__(self) -> str:
        return f"{self.name} ({self.race.name})"


class Guild(models.Model):
    name: str = models.CharField(max_length=255, unique=True)
    description: str = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Player(models.Model):
    nickname: str = models.CharField(max_length=255, unique=True)
    email: str = models.EmailField(max_length=255)
    bio: str = models.CharField(max_length=255)
    race: Race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild: Guild = models.ForeignKey(
        Guild, on_delete=models.SET_NULL, null=True, blank=True
    )
    created_at: timezone.datetime = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.nickname
