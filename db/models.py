from django.db import models


class Race(models.Model):
    NAME_CHOICES = (
        ("orc", "the orcs"),
        ("elf", "the elves"),
        ("human", "humans only"),
        ("dwarf", "blacksmith")
    )
    name = models.CharField(unique=True, max_length=255, choices=NAME_CHOICES)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(unique=True, max_length=255)
    bonus = models.CharField("Describes what kind of bonus is", max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)


class Guild(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(unique=True, max_length=255)
    email = models.EmailField(max_length=255)
    bio = models.CharField("Short biography", max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True)
    crated_at = models.DateTimeField(auto_now_add=True)
