from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        if self.description:
            return f"Race: {self.name} - ({self.description})"
        return f"Race: {self.name}"


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey("Race", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Skill: {self.name} / Bonus: {self.bonus} / Race: {self.race}"


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        if self.description:
            return f"Guild: {self.name} / {self.description}"
        return f"Guild: {self.name}"


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey("Race", on_delete=models.CASCADE)
    guild = models.ForeignKey("Guild", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        guild = self.guild
        if not guild:
            guild = "No Guild"
        return (f"Nickname: {self.nickname}\n"
                f"email: {self.email}\n"
                f"about: {self.bio}\n"
                f"Race: {self.race}\n"
                f"Guild: {guild}\n"
                f"Created: {self.created_at}")
