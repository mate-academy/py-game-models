
from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"Race: {self.name} | Description: {self.description}"


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Skill: {self.name} | Bonus: {self.bonus} | Race: {self.race}"


class Guild(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return f"Guild: {self.name} | Description: {self.description}"


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return (f"Nickname: {self.nickname} | Race: {self.race} | "
                f"Guild: {self.guild}")
