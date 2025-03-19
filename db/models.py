from django.db import models


class Race(models.Model):

    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"Race: {self.name}\nDescription: {self.description}\n"


class Skill(models.Model):

    name = models.CharField(unique=True, max_length=255)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return (
            f"Skill: {self.name}\n"
            f"Bonus: {self.bonus}\n"
            f"Race: {self.race.name}\n"
        )


class Guild(models.Model):

    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"Guild: {self.name}\nDescription: {self.description}\n"


class Player(models.Model):

    nickname = models.CharField(unique=True, max_length=255)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
    )
    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return (
            f"Player name: {self.nickname}\n"
            f"{self.race}"
            f"Created at: {self.created_at}\n"
        )
