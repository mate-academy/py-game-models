from django.db import models


RACES_NAME = [
    ("Elf", "Elf"),
    ("Human", "Human"),
    ("Dwarf", "Dwarf"),
    ("Orc", "Orc")
]


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True, choices=RACES_NAME)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        related_name="skills",
        on_delete=models.CASCADE

    )


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        related_name="players",
        on_delete=models.CASCADE
    )
    guild = models.ForeignKey(
        Guild,
        related_name="players",
        on_delete=models.SET_NULL,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
