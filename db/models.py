from django.db import models
from django.db.models import CharField


class Race(models.Model):
    RACE_NAME = (
        ("elf", "Elf Race"),
        ("dwarf", "Dwarf Race"),
        ("human", "Human Race"),
        ("ork", "Ork Race"),
    )

    name = models.CharField(max_length=255,
                            unique=True,
                            choices=RACE_NAME,
                            default="Unknown")
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild,
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
