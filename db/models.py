from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)  # описание расы, можно пустое

    def __str__(self) -> str:
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)  # бонус навыка
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="skills"  # доступ к навыкам из расы
    )

    def __str__(self) -> str:
        return f"{self.name} ({self.race.name})"


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)  # описание гильдии, можно пустое

    def __str__(self) -> str:
        return self.name


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.TextField(blank=True)  # биография игрока
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="players"  # обратный поиск игроков по расе
    )
    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="players"  # обратный поиск игроков по гильдии
    )
    skills = models.ManyToManyField(
        Skill,
        blank=True,
        related_name="players"  # обратный поиск игроков по навыку
    )
    created_at = models.DateTimeField(auto_now_add=True)  # дата создания

    def __str__(self) -> str:
        return self.nickname
