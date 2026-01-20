from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE,
                             help_text="Shows which race has"
                                       " the corresponding skill")


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE,
                             help_text="Shows the race of the player")
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True,
                              help_text="Stores an id of the guild "
                                        "the player is a member of")
    created_at = models.DateTimeField(auto_now=True)
