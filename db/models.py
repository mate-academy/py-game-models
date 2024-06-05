from django.db import models


class Race(models.Model):
    RACES = [
        ("elf", "Elves - beautiful guardians of the woods"),
        ("dwarf", "Dwarves - don't let their short height fool you!"),
        ("human", "Humans - just like in real life"),
        ("Ork", "Orks - a miserable race of green-skinned creatures")
    ]

    name = models.CharField(max_length=255, unique=True, choices=RACES)
    description = models.TextField(blank=True)

    def __str__(self):
        return dict(self.RACES).get(self.name, "Unknown race")


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    nickname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.SET_NULL, null=True)
    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,
        null=True,
        default="none")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nickname
