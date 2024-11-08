from django.db import models


class Race(models.Model):
    """Model represents type of heroes"""

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return str(self.name)


class Skill(models.Model):
    """Model describes skills for each race"""

    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race, on_delete=models.CASCADE, related_name="skills"
    )

    def __str__(self) -> str:
        return str(self.name)


class Guild(models.Model):
    """Guild model"""

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return str(self.name)


class Player(models.Model):
    """Model represents the player"""

    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race, on_delete=models.CASCADE, related_name="players"
    )
    guild = models.ForeignKey(
        Guild, on_delete=models.SET_NULL, related_name="players", null=True
    )
    created_at = models.DateField(auto_now_add=True)
