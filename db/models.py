from django.db import models


class Race(models.Model):
    RACE_CHOICES = (
        ("Elf", "Race of elfs"),
        ("Dwarf", "Race of dwarfs"),
        ("Human", "Race of people"),
        ("Ork", "Race of russians")
    )

    name = models.CharField(
        max_length=255,
        choices=RACE_CHOICES,
        unique=True
    )
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)


class Guild(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True)
