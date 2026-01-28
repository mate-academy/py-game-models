from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Race: {self.name}"


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name="skills")

    def __str__(self):
        return (f"{self.name}, "
                f"bonus: {self.bonus}, "
                f"race: {self.race.name}")


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Guild: {self.name}"

class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name="players")
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, related_name="players", null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"Player: {self.nickname}, "
                f"race: {self.race.name}, "
                f"skills: {self.race.skills.all()}")
