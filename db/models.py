from django.db import models


class Race(models.Model):
    Race_Choices = (
        ("ELF", "Elf"),
        ("DWARF", "Dwarf"),
        ("HUMAN", "Human"),
        ("ORK", "Ork"),
    )
    name = models.CharField(max_length=255, unique=True, choices=Race_Choices)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True)
    create_at = models.DateTimeField(auto_now=True)
