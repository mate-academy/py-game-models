from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)
    bonus = models.TextField(null=True, blank=True)
    race = models.ForeignKey(
        Race,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="skills",
    )

    def __str__(self) -> str:
        return self.name


class Guild(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Player(models.Model):
    nickname = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True, blank=True)
    race = models.ForeignKey(
        Race,
        on_delete=models.PROTECT,
        related_name="players",
    )
    skills = models.ManyToManyField(Skill, blank=True, related_name="players")
    guild = models.ForeignKey(
        Guild,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="players",
    )

    def __str__(self) -> str:
        return self.nickname
