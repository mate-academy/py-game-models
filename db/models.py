from django.db import models


class Race(models.Model):
    names_for_choose = [
        ("elf", "Elf"),
        ("dwarf", "Dwarf"),
        ("human", "Human")
    ]
    name = models.CharField(
        max_length=255,
        unique=True,
        choices=names_for_choose
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
        Guild,
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(auto_now_add=True)
