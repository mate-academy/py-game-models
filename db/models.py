from django.db import models


class Race(models.Model):
    RACE_TO_PLAY = (
        ("ELF", "Elf"),
        ("DWARF", "Dwarf"),
        ("ORK", "Ork"),
        ("HUMAN", "Human")
    )
    name = models.CharField(max_length=255, unique=True, choices=RACE_TO_PLAY)
    description = models.TextField(null=True, blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True, default=None)
    description = models.TextField(null=True, blank=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255, )
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
