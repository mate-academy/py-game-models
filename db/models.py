from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,
                                   null=True)


class Skill(models.Model):
    name = models.CharField(max_length=255)
    bonus = models.CharField("Describes what kind of bonus players can get",
                             max_length=255)
    race = models.ForeignKey(Race,
                             on_delete=models.CASCADE)


class Guild(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,
                                   null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    bio = models.CharField("Stores a short description provided by a "
                           "user about himself/herself",
                           max_length=255)
    race = models.ForeignKey(Race,
                             on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild,
                              on_delete=models.CASCADE,
                              null=True)  # TODO null?
    created_at = models.DateField(auto_now_add=True)
