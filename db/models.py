from django.db import models


class Race(models.Model):
    name: str = models.CharField(max_length=255, unique=True)
    description: str = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Skill(models.Model):
    name: str = models.CharField(max_length=255, unique=True)
    bonus: str = models.CharField(max_length=255)
    race: Race = models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Guild(models.Model):
    name: str = models.CharField(max_length=255, unique=True)
    description: str = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Player(models.Model):
    nickname: str = models.CharField(max_length=255, unique=True)
    email: str = models.EmailField(max_length=255)
    bio: str = models.CharField(max_length=255)
    race: Race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild: Guild = models.ForeignKey(
        Guild, on_delete=models.SET_NULL, null=True, blank=True
    )
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nickname
