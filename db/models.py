from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"name: {self.name}, description: {self.description}"


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        related_name="skills",
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"name: {self.name}, bonus: {self.bonus}, race: {self.race}"


class Guild(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return f"name: {self.name}, description: {self.description}"


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        related_name="players",
        on_delete=models.CASCADE
    )
    guild = models.ForeignKey(
        Guild,
        related_name="players",
        on_delete=models.SET_NULL,
        null=True
    )
    created_at = models.DateField(auto_now_add=True)
