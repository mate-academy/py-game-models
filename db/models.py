from django.db import models


class Race(models.Model):
    ELF = "Elf"
    DWARF = "Dwarf"
    HUMAN = "Human"
    ORK = "Ork"
    RACE_CHOICES = [
        (ELF, "Elf"),
        (DWARF, "Dwarf"),
        (HUMAN, "Human"),
        (ORK, "Ork"),
    ]
    name = models.CharField(max_length=255, unique=True, choices=RACE_CHOICES)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"Race: {self.name}"


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(
        "kind of bonus players can get from a possession of the skill",
        max_length=255
    )
    race = models.ForeignKey(Race, to_field="name", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.race} has {self.name} skill"


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return f"Guild: {self.name}"


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(
        "short description provided by a user about himself/herself",
        max_length=255,
    )
    race = models.ForeignKey(
        Race,
        to_field="name",
        on_delete=models.CASCADE,
    )
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Player: {self.nickname}"
