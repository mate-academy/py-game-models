from django.db import models


RACE_CHOOSE = (
    ("Elf", "elf"),
    ("Dwarf", "dwarf"),
    ("Human", "human"),
    ("Ork", "ork"),
)


class Race(models.Model):
    name = models.CharField(max_length=255, choices=RACE_CHOOSE, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"This is {self.name} race. {self.description}"


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"This is {self.name} skill. {self.bonus}"


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return f"This is {self.name} guild. {self.description}"


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Player {self.nickname}  {self.email}"
