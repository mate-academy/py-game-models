from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"#{self.id} {self.name}: {self.description}"


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self):
        return f"#{self.id} {self.name} ({self.race}): {self.bonus}"


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)

    def __str__(self):
        return f"#{self.id} {self.name}: {self.description}"


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"#{self.id} {self.nickname} ({self.race})"
