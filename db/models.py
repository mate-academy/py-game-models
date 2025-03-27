from django.db import models


class Race(models.Model):
    NAME_CHOICES = (
        ("elf", "Elf race"),
        ("dwarf", "Dwarf race"),
        ("human", "Human race"),
        ("ork", "Ork race")
    )
    name = models.CharField(max_length=255, unique=True, choices=NAME_CHOICES)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField("Kind of bonus players can get from the skill",
                             max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField("Short description by user about himself/herself",
                           max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Player '{self.nickname}' created at: {self.created_at}"
