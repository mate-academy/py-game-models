from django.db import models

RACE_CHOICES = (
    ("elf", "Elf"),
    ("dwarf", "Dwarf"),
    ("human", "Human"),
    ("ork", "Ork"),
)


class Race(models.Model):
    name = models.CharField(max_length=255, choices=RACE_CHOICES, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.name} {self.description}"


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name} {self.bonus} {self.race}"


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return f"{self.name} {self.description}"


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return (f"{self.nickname} {self.email} {self.bio} \n "
                f"{self.race} {self.guild} {self.created_at}")
