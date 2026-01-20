from django.db import models


class Race(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"Race #{self.id}: {self.name}. {self.description}"


class Skill(models.Model):
    name = models.CharField(unique=True, max_length=255)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.race} skill #{self.id}: {self.name}. {self.bonus}"


class Guild(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return f"Guild #{self.id}: {self.name}. " \
               f"{self.description if self.description is not None else ''}"


class Player(models.Model):
    nickname = models.CharField(unique=True, max_length=255)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        guild_message = self.guild or "Does not belong to any guilds"

        return f"Player #{self.id}: {self.nickname}. " \
               f"Email: {self.email}.\n" \
               f"{self.bio}.\n" \
               f"{self.race}\n" \
               f"{guild_message}\n" \
               f"Created at: {self.create_at}"
