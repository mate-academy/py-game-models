from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)  # Correto para campos de texto opcionais

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name='skills')  # Deleta skills ao deletar a raça

    def __str__(self):
        return self.name


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)  # Correção: usar blank=True, não null=True

    def __str__(self):
        return self.name


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name='players')  # Deleta player com a raça
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True, blank=True, related_name='players')  # Não deleta player se guild for deletada
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nickname
