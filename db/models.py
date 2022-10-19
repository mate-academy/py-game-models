from django.db import models


class Race(models.Model):
    ROLES_CHOICES = (
        ("Elf", "race to play: Elf"),
        ("Dwarf", "race to play: Dwarf"),
        ("Human", "race to play: Human"),
        ("Ork", "race to play: Ork")
    )
    name = models.CharField(max_length=255, choices=ROLES_CHOICES, unique=True)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True, default=None)
    description = models.TextField(blank=True, null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
