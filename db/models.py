from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(
        "This field describes what kind of bonus players can get from it.",
        max_length=255, blank=True)
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="skill_race"
    )


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(
        "Short description provided by a user about himself/herself.",
        max_length=255)
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="race"
    )
    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,
        null=True,
        related_name="guild"
    )
    created_at = models.DateTimeField(auto_now_add=True)
