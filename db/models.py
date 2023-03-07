from __future__ import annotations

from django.db import models

races = (
    ("Elf", "Elf"),
    ("Dwarf", "Dwarf"),
    ("Human", "Human"),
    ("Ork", "Ork"),
)


class Race(models.Model):
    name = models.CharField(max_length=255, choices=races, unique=True)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(
        Guild, on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    created_at = models.DateField(auto_now=True)
