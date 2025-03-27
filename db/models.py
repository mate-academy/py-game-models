from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Guild(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return self.name


class Player(models.Model):
    nickname = models.CharField(
        max_length=255,
        unique=True
    )
    email = models.EmailField()
    bio = models.TextField()
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="players"
    )
    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,
        related_name="players",
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self) -> str:
        return self.nickname
