from django.db import models as m


class Race(m.Model):
    races = (
        ("E", "Elf"),
        ("D", "Dwarf"),
        ("H", "Human"),
        ("O", "Ork")
    )

    name = m.CharField(max_length=255, unique=True, choices=races)
    description = m.TextField(blank=True)

    def __str__(self) -> str:
        return f"The race is:{self.name}"


class Skill(m.Model):
    name = m.CharField(max_length=255, unique=True)
    bonus = m.CharField(max_length=255)
    race = m.ForeignKey(Race, on_delete=m.PROTECT)

    def __str__(self) -> str:
        return f"Skill: {self.name}, belongs to {self.race.name}"


class Guild(m.Model):
    name = m.CharField(max_length=255, unique=True)
    description = m.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"Guild {self.name}!"


class Player(m.Model):
    nickname = m.CharField(max_length=255, unique=True)
    email = m.EmailField(max_length=255)
    bio = m.CharField(max_length=255)
    race = m.ForeignKey(Race, on_delete=m.PROTECT)
    guild = m.ForeignKey(Guild, on_delete=m.PROTECT, null=True)
    create_at = m.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return (f"Name: {self.nickname}, "
                f"race: {self.race.name}, "
                f"guild: {self.guild.name}")
