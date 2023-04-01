from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.name}. {self.description}"


class Skill(models.Model):
    name = models.CharField(unique=True, max_length=255)
    bonus = models.CharField(
        "Describes what kind of bonus players can get from it",
        max_length=255
    )
    race = models.ForeignKey(
        "Race",
        related_name="skill_set",
        on_delete=models.DO_NOTHING
    )

    def __str__(self) -> str:
        return f"{self.name} (bonus: {self.bonus}, race: {self.race.name})"


class Guild(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return self.name


class Player(models.Model):
    nickname = models.CharField(unique=True, max_length=255)
    email = models.EmailField(max_length=255)
    bio = models.CharField(
        "Stores a short description provided by a user about himself/herself.",
        max_length=255
    )
    race = models.ForeignKey(
        "Race",
        related_name="player_race",
        on_delete=models.DO_NOTHING
    )
    guild = models.ForeignKey(
        "Guild",
        related_name="player_guild",
        on_delete=models.SET_NULL,
        null=True
    )
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.nickname}, {self.email}. {self.bio}. " \
               f"Race: {self.race}. Guild: {self.guild}."
