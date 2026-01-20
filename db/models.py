from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, default="")

    def __str__(self) -> str:
        return self.name


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255, blank=True, default="")
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True, blank=True)
    bio = models.CharField(max_length=255, blank=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(
        Guild, on_delete=models.SET_NULL, null=True, blank=True
    )
    skills = models.ManyToManyField(
        Skill,
        related_name="players"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nickname
