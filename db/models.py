from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    # The skill must be deleted when the race is deleted
    race = models.ForeignKey(
        Race, on_delete=models.CASCADE, related_name="skills"
    )

    def __str__(self) -> str:
        return f"{self.name} ({self.race.name})"


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    # Can be null means null=True.
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    # Player must be deleted when the race is deleted
    race = models.ForeignKey(
        Race, on_delete=models.CASCADE, related_name="players"
    )
    # Player should NOT be deleted when the guild is deleted
    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="members",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nickname
