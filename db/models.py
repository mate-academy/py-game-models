from django.db import models
from django.utils import timezone


class Race(models.Model):
    RACES = [
        ("Elf", "Elf"),
        ("Dwarf", "Dwarf"),
        ("Human", "Human"),
        ("Ork", "Ork")
    ]

    name = models.CharField(
        max_length=255,
        unique=True,
        choices=RACES
    )
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
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
        Race,
        on_delete=models.CASCADE,
        related_name="races"
    )
    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,
        null=True,
        related_name="guilds"
    )
    created_at = models.DateTimeField(
        default=timezone.now
    )
