from django.db import models


class Race(models.Model):
    RACE_NAME_CHOICES = (
        ("elf", "Elf"),
        ("dwarf", "Dwarf"),
        ("human", "Human"),
        ("ork", "Ork")
    )
    name = models.CharField(
        choices=RACE_NAME_CHOICES,
        unique=True,
        max_length=255
    )
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(unique=True, max_length=255)
    bonus = models.CharField(
        "Bonus describes what kind of bonus player can get from skill",
        max_length=255
    )
    race = models.ForeignKey(Race, on_delete=models.CASCADE)


class Guild(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(unique=True, max_length=255)
    email = models.EmailField(max_length=255)
    bio = models.CharField(
        "Bio stores a short description about user provided by himself",
        max_length=255
    )
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
