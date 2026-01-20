from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return (
            f"Race: name = {self.name}, "
            f"description = {self.description}"
        )


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return (
            f"Skill: name = {self.name}, "
            f"bonus = {self.bonus}, "
            f"race = {self.race}"
        )


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return (
            f"Guild: name = {self.name}, "
            f"description = {self.description}"
        )


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.SET_NULL, null=True)
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return (
            f"""
            Player: nickname = {self.nickname},
            email = {self.email},
            bio = {self.bio},
            race = {self.race},
            guild = {self.guild}
            """
        )
