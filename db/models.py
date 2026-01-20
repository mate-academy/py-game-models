from django.db import models
from django.db.models import TextField


class Race(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(unique=True, max_length=255)
    bonus = models.CharField(
        max_length=255,
        help_text="Description of the bonus."
    )
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="skills"
    )


class Guild(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = TextField(default=None, null=True, blank=True)


class Player(models.Model):
    nickname = models.CharField(unique=True, max_length=255)
    email = models.EmailField(max_length=255)
    bio = models.CharField(
        max_length=255,
        help_text="Short description about player."
    )
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="race"
    )
    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
        related_name="players"
    )
    created_at = models.DateTimeField(auto_now_add=True)
