from django.db import models


class Race(models.Model):
    class RaceNames(models.TextChoices):
        ELF = "ELF", "Elf"
        DWARF = "DWARF", "Dwarf"
        HUMAN = "HUMAN", "Human"
        ORK = "ORK", "Ork"

    name = models.CharField(unique=True,
                            max_length=255,
                            choices=RaceNames.choices)
    description = models.TextField(blank=True, null=True)


class Skill(models.Model):
    name = models.CharField(unique=True, max_length=255)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race,
                             on_delete=models.CASCADE,
                             related_name="skills")


class Guild(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(unique=True, max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    bio = models.CharField(max_length=255, blank=True, null=True)
    race = models.ForeignKey(Race,
                             on_delete=models.CASCADE,
                             related_name="players")
    guild = models.ForeignKey(Guild,
                              null=True,
                              on_delete=models.SET_NULL,
                              related_name="players")
    created_at = models.DateTimeField(auto_now_add=True)
