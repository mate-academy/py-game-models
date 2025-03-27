from django.db import models


class Race(models.Model):
    RACE_CHOICES = [
        ("Elf", "Elf"),
        ("Dwarf", "Dwarf"),
        ("Human", "Human"),
        ("Ork", "Ork")
    ]
    name = models.CharField(max_length=255, unique=True, choices=RACE_CHOICES)
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
    email = models.EmailField(unique=False)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="player_set"
    )
    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,
        null=True,
        related_name="player_set"
    )
    created_at = models.DateTimeField(auto_now_add=True)
