from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.description})"


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255, blank=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE,
                             related_name="skills")

    def __str__(self) -> str:
        return f"{self.name} ({self.race})"


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.description or "No description"})"


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255, blank=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE,
                             related_name="players")
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL,
                              null=True, related_name="players",
                              default=None)
    created_at = models.DateTimeField(auto_now_add=True)
