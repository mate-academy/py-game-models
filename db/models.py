from django.db import models


class Race(models.Model):
    class RaceType(models.TextChoices):
        ELF = ("elf", "The elf race")
        DWARF = ("dwarf", "The dwarf race")
        HUMAN = ("human", "Human race")
        ORK = ("ork", "The ork race")

    name = models.CharField(
        max_length=255,
        unique=True,
        choices=RaceType.choices
    )
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.description}"


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name} - {self.bonus}"


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return f"{self.name} {self.description or ''}"


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.nickname.capitalize()} - {self.bio}"
