from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name + self.description


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(
        "This field describes what kind of bonus players can get from it.",
        max_length=255
    )
    race = models.ForeignKey(Race, on_delete=models.CASCADE)


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(
       "It stores a short description provided by a user about himself/herself.",
       max_length=255
    )
    race = models.ForeignKey(Race, models.CASCADE)
    guild = models.ForeignKey(Guild, models.SET_NULL, null=True)
    created_at = models.DateField(auto_now_add=True)
