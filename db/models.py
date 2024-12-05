from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"Name: {self.name}, Description: {self.description}"


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255, null=True, default=None)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Name: {self.name}, Bonus: {self.bonus}, Race: {self.race}"


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, default=None)


class Player(models.Model):
    nickname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(
        Guild, null=True, default=None, on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.nickname}"
