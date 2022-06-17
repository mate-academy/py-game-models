from django.db import models

CHAR_LENGTH = 255


class Race(models.Model):
    name = models.CharField(max_length=CHAR_LENGTH, unique=True)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=CHAR_LENGTH, unique=True)
    bonus = models.CharField("what kind of bonus players can get from it",
                             max_length=CHAR_LENGTH)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)


class Guild(models.Model):
    name = models.CharField(max_length=CHAR_LENGTH, unique=True)
    description = models.TextField(null=True, blank=True)


class Player(models.Model):
    nickname = models.CharField(unique=True, max_length=CHAR_LENGTH)
    email = models.EmailField(max_length=CHAR_LENGTH)
    bio = models.CharField("It stores a short description provided "
                           "by a user about himself/herself",
                           max_length=CHAR_LENGTH)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True)
