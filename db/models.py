from __future__ import annotations

from django.db import models


class Race(models.Model):
    RACE_CHOICE = (
        ("Elf", "Elf"),
        ("Dwarf", "Dwarf"),
        ("Human", "Human"),
        ("Ork", "Ork")
    )

    name = models.CharField(
        max_length=255,
        choices=RACE_CHOICE,
        unique=True
    )
    description = models.TextField(blank=True, null=True)

    @classmethod
    def race_import(
            cls,
            race_name: str,
            race_description: str
    ) -> Race:

        if cls.objects.filter(name=race_name).exists():
            return cls.objects.get(name=race_name)

        return cls.objects.create(name=race_name,
                                  description=race_description)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

    @classmethod
    def skill_import(
            cls,
            skill_name: str,
            skill_bonus: str,
            skill_race: Race
    ) -> Skill:

        if cls.objects.filter(name=skill_name).exists():
            return cls.objects.get(name=skill_name)

        return cls.objects.create(
            name=skill_name,
            bonus=skill_bonus,
            race=skill_race
        )


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    @classmethod
    def guild_import(
            cls,
            guild_name: str,
            guild_description: str
    ) -> Guild:

        if cls.objects.filter(name=guild_name).exists():
            return cls.objects.get(name=guild_name)

        return cls.objects.create(
            name=guild_name,
            description=guild_description
        )


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(
        Guild,
        null=True,
        on_delete=models.SET_NULL,
        related_name="players"
    )
    created_at = models.DateTimeField(auto_now_add=True)
