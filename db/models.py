from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255,
                             blank=True,
                             null=True,
                             default=None)
    race = models.ForeignKey(Race,
                             on_delete=models.CASCADE,
                             related_name="skill")


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True, default=None)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255, blank=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE,
                             related_name="player_race")
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL,
                              null=True,
                              default=None,
                              related_name="player_guild")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nickname
