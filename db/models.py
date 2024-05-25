from django.db import models


class Race(models.Model):
    RACE_CHOICES = (
        ("Elf", "being with magical powers and supernatural beauty"),
        ("Dwarf", "living in mountains or stones "
                  "and being skilled craftspeople"),
        ("Human", "most common and widespread species of primate"),
        ("Ork", "a demon of Tyrol alpine folklore")
    )
    name = models.CharField(max_length=255, unique=True, choices=RACE_CHOICES)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.RESTRICT)


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
