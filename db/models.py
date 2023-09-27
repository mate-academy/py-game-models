from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return (f"name: {self.name}\n"
                f"description: {self.description}")


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(
        "kind of bonus players can get from it",
        max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (f"name: {self.name}\n"
                f"bonus: {self.bonus}\n"
                f"race: {self.race}")


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return (f"name: {self.name}\n"
                f"description: {self.description}")


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(
        "It stores a short description "
        "provided by a user about himself/herself",
        max_length=255
    )
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,
        null=True,
        default=None)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return (f"nickname: {self.nickname}\n"
                f"email: {self.email}\n"
                f"bio: {self.bio}\n"
                f"race: {self.race}\n"
                f"guild: {self.guild}\n"
                f"created_at: {self.created_at}")
