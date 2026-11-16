from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(
        max_length=255,
        help_text="""This field descrubes what kind of bonus players
        can get from it. In other words, this is a description of the bonus"""
    )
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)
