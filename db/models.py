from django.db import models


class Race(models.Model):
    race_choice = (
        ("ELF", "Elf"),
        ("ORK", "Ork"),
        ("HUMAN", "Human"),
        ("DWARF", "Dwarf")
    )

    name = models.CharField(max_length=255, choices=race_choice, default=None)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.name} {self.description}"


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race,
                             on_delete=models.CASCADE,
                             related_name="skill_set")

    def __str__(self) -> str:
        return f"{self.name} {self.bonus}"


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name} {self.description}"


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.TextField(max_length=255)
    race = models.ForeignKey(Race,
                             on_delete=models.CASCADE,
                             related_name="skills")
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.nickname} {self.email} {self.bio} {self.created_at}"
