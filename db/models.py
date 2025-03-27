from django.db import models


class Race(models.Model):
    race_to_choose = [
        ("Elf", "Elf"),
        ("Dwarf", "Dwarf"),
        ("Human", "Human"),
        ("Ork", "Ork")
    ]

    name = models.CharField(
        max_length=255,
        unique=True,
        choices=race_to_choose
    )
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True
    )
    bonus = models.CharField(
        "what kind of bonus players can get from skill",
        max_length=255
    )
    race = models.ForeignKey(Race, on_delete=models.CASCADE)


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(
        "short description provided by a user about himself/herself",
        max_length=255
    )
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
