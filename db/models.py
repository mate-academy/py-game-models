from django.db import models


class Race(models.Model):
    races = [
        ("e", "elf"),
        ("d", "dwarf"),
        ("h", "human"),
        ("o", "ork")
    ]
    name = models.CharField(unique=True, max_length=255, choices=races)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(unique=True, max_length=255)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE
    )


class Guild(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)


class Player(models.Model):
    nickname = models.CharField(unique=True, max_length=255)
    email = models.EmailField(max_length=255)
    bio = models.TextField()
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE
    )
    guild = models.ForeignKey(
        Guild,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now=True)
