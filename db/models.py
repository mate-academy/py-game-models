from django.db import models


class Race(models.Model):
    RACE_CHOICES = [
        ("E", "Elf"),
        ("D", "Dwarf"),
        ("H", "Human"),
        ("O", "Ork"),
    ]
    name = models.CharField(unique=True, max_length=255, choices=RACE_CHOICES)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(unique=True, max_length=255)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)


class Guild(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(unique=True, max_length=255)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
