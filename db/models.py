from django.db import models


class Race(models.Model):
    NAMES_CHOICES = [
        ("ELF", "Elf"),
        ("DWARF", "Dwarf"),
        ("HUMAN", "Human"),
        ("ORK", "Ork")
    ]
    name = models.CharField(
        max_length=255,
        unique=True,
        choices=NAMES_CHOICES
    )
    description = models.TextField(blank=True, null=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="skill_set"
    )


class Guild(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(unique=True, max_length=255)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="players"
    )
    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,
        null=True,
        related_name="players"
    )
    created_at = models.DateTimeField(auto_now_add=True)
