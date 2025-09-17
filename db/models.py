from django.db import models


class Race(models.Model):
    RACES = (
        ("Elf", "Elf race"),
        ("Dwarf", "Dwarf race"),
        ("Human", "Human race"),
        ("Ork", "Ork race"),
    )
    name = models.CharField(max_length=255, unique=True, choices=RACES)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(
        "This field describes what kind of bonus players can get from it.",
        max_length=255, blank=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(
        "Short description provided by a user about himself/herself.",
        max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True)  # or DO_NOTHING
    created_at = models.DateTimeField(auto_now_add=True)
