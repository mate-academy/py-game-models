from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    # Exigência: "pode estar em branco" -> apenas blank=True
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    # Exigência: related_name="skills"
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="skills"
    )

    def __str__(self) -> str:
        return self.name


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    # Exigência: "pode ser nulo" -> apenas null=True
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return self.name


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    # Exigência: related_name="players"
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="players"
    )
    # Exigência: related_name="players"
    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="players"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nickname
