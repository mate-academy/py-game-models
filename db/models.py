from django.db import models
from django.utils import timezone


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(
        max_length=255,
        help_text="This field describes "
                  "what kind of bonus players can get from it."
    )
    race = models.ForeignKey(
        Race, on_delete=models.CASCADE,
        help_text="It shows which race has the corresponding skill."
    )


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(
        max_length=255,
        help_text="It stores a short description"
                  " provided by a user about himself/herself."
    )
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True)
    created_at = models.DateField(default=timezone.now())
