from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.name}: {self.description}"


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (
            f"Skill: {self.name}. "
            f"Bonus: {self.bonus}."
            f"(Race: {self.race.name})"
        )


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return f"Guild: {self.name}. {self.description}"


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(
        "provided by a user about himself/herself.",
        max_length=255,
    )
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True)
    created_st = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return (
            f"{self.nickname}: "
            f"{self.email}. "
            f"BIO '{self.bio}. "
            f"Race: {self.race.name}, {self.race.description}"
        )
