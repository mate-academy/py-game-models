from django.db import models

# Модель Guild
class Guild(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Race(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# Модель Skill
class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name='skills')  # Добавлено related_name

    def __str__(self):
        return self.name

# Модель Player
class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    bio = models.TextField()
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nickname