from django.db import models


class Race (models.Model):
    RACE_FIELD = (
        ("Ork", "ork"),
        ("Elf", "elf"),
        ("Dwarf", "dwarf"),
        ("Human", "human"),
    )
    name = models.CharField(max_length=255, choices=RACE_FIELD, unique=True)
    description = models.TextField(blank=True)


class Skill (models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(
        "Describes what kind of bonus players can get from it",
        max_length=255
    )
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="skills"
    )


class Guild (models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)


class Player (models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(
        "It stores a short description provided "
        "by a user about himself/herself.",
        blank=True,
        max_length=255
    )
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="players"
    )
    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,
        null=True,
        related_name="players",
    )
    created_at = models.DateTimeField(auto_now_add=True)
