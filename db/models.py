from django.db import models


class Race(models.Model):
    COURSE_CHOICES = (
        ("ELF", "Elf course"),
        ("DWARF", "Dwarf course"),
        ("HUMAN", "Human course"),
        ("ORK", "Ork course"),
    )

    name = models.CharField(
        max_length=255,
        unique=True,
        choices=COURSE_CHOICES
    )
    description = models.TextField(blank=True, null=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(
        Guild, null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(auto_now=True)
