from django.db import models
from django.utils import timezone

# 1. Race Model
class Race(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Nazwa Rasy"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Opis Rasy"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Rasa"
        verbose_name_plural = "Rasy"
        # USUNIĘTO: ordering = [...]

# 2. Skill Model
class Skill(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Nazwa Umiejętności"
    )
    bonus = models.CharField(
        max_length=255,
        verbose_name="Opis Bonusu"
    )
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name='skills',
        verbose_name="Rasa"
    )

    def __str__(self):
        return f"{self.name} ({self.race.name})"

    class Meta:
        verbose_name = "Umiejętność"
        verbose_name_plural = "Umiejętności"
        # USUNIĘTO: ordering = [...]


# 3. Guild Model
class Guild(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Nazwa Gildii"
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Opis Gildii"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Gildia"
        verbose_name_plural = "Gildie"
        # USUNIĘTO: ordering = [...]


# 4. Player model
class Player(models.Model):
    nickname = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Pseudonim"
    )
    email = models.EmailField(
        max_length=255,
        verbose_name="Email"
    )
    bio = models.CharField(
        max_length=255,
        verbose_name="Krótki Opis (Bio)"
    )
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name='players',
        verbose_name="Rasa Gracza"
    )
    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='members',
        verbose_name="Gildia"
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="Data Utworzenia"
    )

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = "Gracz"
        verbose_name_plural = "Gracze"
        # USUNIĘTO: ordering = [...]
