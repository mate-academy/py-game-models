from django.db import models
from django.utils import timezone


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,  # habilidade é deletada quando a Race é deletada
        related_name="skills",
    )

    def __str__(self):
        return f"{self.name} ({self.race.name})"


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)

    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,  # jogador é deletado quando a Race é deletada
        related_name="players",
    )
    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,  # jogador NÃO é deletado se a guilda for apagada
        null=True,
        related_name="players",
    )

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nickname
