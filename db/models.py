from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> any:
        return f"{self.name}, description: {self.description}"


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE,
                             related_name="skill_set")

    def __str__(self) -> any:
        return f"{self.name} (bonus: {self.bonus}), race: {self.race.name}"


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)

    def __str__(self) -> any:
        return f"{self.name}, description: {self.description}"


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=False)
    bio = models.CharField(max_length=255, blank=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE,
                             related_name="players")
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL,
                              null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> any:
        return (f"{self.nickname}, email: {self.email}, "
                f"bio: {self.bio}, created: {self.created_at}")
