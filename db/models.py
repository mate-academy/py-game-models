from django.db import models


class Race(models.Model):
    races_list = (
        ("elf", "a race of elves"),
        ("dwarf", "a race of dwarfs"),
        ("human", "human race"),
        ("ork", "the ork race")
    )
    name = models.CharField(
        max_length=255,
        unique=True,
        choices=races_list
    )
    description = models.TextField(blank=True, null=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE, null=True)


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE, null=True)
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
