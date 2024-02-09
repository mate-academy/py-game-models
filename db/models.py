from django.db import models


class Race(models.Model):
    RACES = [
        ("elf", "Elf"),
        ("dwarf", "Dwarf"),
        ("human", "Human"),
        ("ork", "Ork")
    ]
    name = models.CharField(unique=True, max_length=255, choices=RACES)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"Race: {self.get_name_display()}"


class Skill(models.Model):
    name = models.CharField(max_length=255)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="skills"
    )

    def __str__(self) -> str:
        return f"{self.name}, bonus: {self.bonus}"


class Guild(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return f"Guild: {self.name}"


class Player(models.Model):
    nickname = models.CharField(unique=True, max_length=255)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="players"
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
            f"Player: {self.nickname}, "
            f"{self.race}, "
            f"{self.guild}, "
            f"created at {self.created_at}"
        )
