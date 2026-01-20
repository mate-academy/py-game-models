from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    @classmethod
    def get_or_create(cls, race_dict: dict) -> "Race":
        try:
            return cls.objects.get(name=race_dict["name"])
        except ObjectDoesNotExist:
            return cls.objects.create(
                name=race_dict["name"],
                description=race_dict["description"]
            )

    def __str__(self) -> str:
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.TextField()
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="skills"
    )

    @classmethod
    def get_or_create(cls, **kwargs) -> "Skill":
        try:
            return cls.objects.get(name=kwargs["name"])
        except ObjectDoesNotExist:
            return cls.objects.create(
                name=kwargs["name"],
                bonus=kwargs["bonus"],
                race=kwargs["race"]
            )

    def __str__(self) -> str:
        return f"{self.name} {self.race.name}"


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    @classmethod
    def get_or_create(cls, guild_dict: dict) -> "Guild" or None:
        if guild_dict:
            try:
                return cls.objects.get(name=guild_dict["name"])
            except ObjectDoesNotExist:
                return cls.objects.create(
                    name=guild_dict["name"],
                    description=guild_dict["description"]
                )

        return None

    def __str__(self) -> str:
        return self.name


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="players"
    )
    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,
        null=True,
        related_name="players"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.nickname} {self.race.name}"
