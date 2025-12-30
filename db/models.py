from django.db import models


class Race(models.Model):
    """A model to choose a race to play"""
    RACE_TO_PLAY_CHOICES = (
        ("Elf", "Player of elf race"),
        ("Dwarf", "Player of dwarf race"),
        ("Human", "Player of human race"),
        ("Ork", "Player of ork race")
    )
    name = models.CharField(
        max_length=255,
        choices=RACE_TO_PLAY_CHOICES,
        unique=True
    )
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Skill(models.Model):
    """A model to keep race skills"""
    name = models.CharField(
        max_length=255,
        unique=True
    )
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race, on_delete=models.CASCADE
    )


class Guild(models.Model):
    """A model to keep guilds"""
    name = models.CharField(
        max_length=255,
        unique=True
    )
    description = models.TextField(null=True)


class Player(models.Model):
    """A model to create player"""
    nickname = models.CharField(
        max_length=255,
        unique=True
    )
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race, on_delete=models.CASCADE
    )
    guild = models.ForeignKey(
        Guild, on_delete=models.SET_NULL, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
