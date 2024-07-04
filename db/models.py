from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField("kind of bonus players can get", max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"({self.name} {self.bonus})"


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"({self.name} {self.description})"


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race, on_delete=models.CASCADE, null=True, blank=True
    )
    guild = models.ForeignKey(
        Guild, on_delete=models.SET_NULL, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"({self.nickname} {self.bio})"
