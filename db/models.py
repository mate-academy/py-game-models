from django.db import models


class Race(models.Model):
    races = (
        ("E", "Elf"),
        ("D", "Dwarf"),
        ("H", "Human"),
        ("O", "Ork")
    )

    name = models.CharField(max_length=255, unique=True, choices=races)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"The race is: {self.name}"


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Skill: {self.name}, belongs to {self.race.name}"


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"Guild: {self.name}!"


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.PROTECT)
    guild = models.ForeignKey(Guild, on_delete=models.PROTECT, null=True)
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return (f"Name: {self.nickname}, "
                f"race: {self.race.name}, "
                f"guild: {self.guild.name}")
