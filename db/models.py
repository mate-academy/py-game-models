from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# Модель `Skill`, яка містить нове поле `race`
class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    bonus = models.IntegerField(default=0)

    # Додаємо поле race як зовнішній ключ на модель Race
    race = models.ForeignKey(Race, on_delete=models.CASCADE, default=1)  # Вказуємо значення за замовчуванням

    def __str__(self):
        return self.name


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(default="No description provided")

    def __str__(self):
        return self.name


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(blank=True, null=True)
    bio = models.TextField(blank=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nickname
