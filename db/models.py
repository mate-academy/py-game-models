from django.db import models


class NameDescriptionModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name


class Race(NameDescriptionModel):
    pass


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(
        to="Race",
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.name


class Guild(NameDescriptionModel):
    pass


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(
        to="Race",
        related_name="players",
        on_delete=models.CASCADE
    )
    guild = models.ForeignKey(
        to="Guild",
        related_name="players",
        on_delete=models.SET_NULL,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nickname
