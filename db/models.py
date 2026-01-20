from django.db import models


class Race(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True
    )
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"name: {self.name}, description: {self.description}"


class Skill(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True
    )
    bonus = models.CharField(
        "This field describes what kind of bonus players can get from it.",
        max_length=255
    )
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return (
            f"name: {self.name}, "
            f"bonus: {self.bonus}, "
            f"race: {self.race.name}"
        )


class Guild(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        null=True
    )
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return (
            f"name: {self.name}, "
            f"description: {self.description}"
        )


class Player(models.Model):
    nickname = models.CharField(
        max_length=255,
        unique=True
    )
    email = models.EmailField(
        max_length=255,
        unique=True
    )
    bio = models.CharField(
        "It stores a short description "
        "provided by a user about himself/herself.",
        max_length=255
    )
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE
    )
    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return (
            f"name: {self.name}, "
            f"email: {self.email}, "
            f"bio: {self.bio}, "
            f"race: {self.race.name}, "
            f"guild: {self.guild.name}, "
            f"created_at: {self.created_at}, "
        )
