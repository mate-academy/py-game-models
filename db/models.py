from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(unique=True, max_length=255)
    bonus = models.TextField(blank=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)


class Guild(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(unique=True, max_length=255)
    email = models.EmailField(max_length=255)
    bio = models.TextField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE, null=True)
    guild = models.ForeignKey(Guild, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nickname
