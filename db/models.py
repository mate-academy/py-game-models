from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, default="")

    def __str__(self) -> str:
        return self.name


class Guild(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, default="")

    def __str__(self) -> str:
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    bonus = models.TextField(blank=True, default="")
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="skills"
    )

    def __str__(self) -> str:
        return f"{self.name} ({self.bonus})"


class Player(models.Model):
    nickname = models.CharField(max_length=100, unique=True)
    email = models.EmailField(blank=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    race = models.ForeignKey(
        Race,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="players"
    )
    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="players"
    )

    def __str__(self) -> str:
        return self.nickname
