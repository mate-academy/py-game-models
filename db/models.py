from django.db import models


class Race(models.Model):
    RACE_TYPES = (
        ("Elf", "They have big and pointed ears"),
        ("Dwarf", "They are short in stature and constantly mine gold"),
        ("Human", "think they are smarter than others"),
        ("Ork", "creepy freaks who want to kill everyone")
    )

    name = models.CharField(max_length=255, choices=RACE_TYPES, unique=True)
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
    email = models.EmailField(max_length=255, unique=True)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
