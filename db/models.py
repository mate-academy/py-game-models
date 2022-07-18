from django.db import models


class Race(models.Model):
    RACE_CHOICES = (
        ("elf", "Elf"),
        ("dwarf", "Dwarf"),
        ("human", "Human"),
        ("ork", "Ork")
    )
    name = models.CharField(max_length=255, unique=True, choices=RACE_CHOICES)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(
        "This field describes what kind of bonus players can get from it.",
        max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Guild(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(
        "It stores a short description "
        "provided by a user about himself/herself.",
        max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nickname} is {self.race.name} in {self.guild.name}"
