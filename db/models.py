from django.db import models
from django.db.models import DateTimeField


class Race(models.Model):
    race_choice = [
        ("Elf", "Elf"),
        ("Dwarf", "Dwarf"),
        ("Human", "Human"),
        ("Ork", "Ork")
    ]
    name = models.CharField(
        max_length=255,
        unique=True,
        choices=race_choice
    )
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        related_name="skill_set",
        on_delete=models.CASCADE
    )


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, default="<EMAIL>")
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        related_name="players",
        on_delete=models.CASCADE
    )
    guild = models.ForeignKey(
        Guild,
        related_name="members",
        null=True,
        on_delete=models.SET_NULL
    )
    created_at = DateTimeField(auto_now_add=True)
