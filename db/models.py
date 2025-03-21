from django.db import models


class Race(models.Model):
    """
    Модель Race представляет расы,
     которые могут выбирать игроки.
    """
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Skill(models.Model):
    """
    Модель Skill представляет навыки,
     которые могут быть у рас.
    """
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE,
                             related_name="skills")

    def __str__(self) -> str:
        return self.name


class Guild(models.Model):
    """
    Модель Guild представляет гильдии,
     к которым могут присоединяться игроки.
    """
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Player(models.Model):
    """
    Модель Player представляет игрока.
    """
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE,
                             related_name="players")
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True,
                              blank=True, related_name="players")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nickname
