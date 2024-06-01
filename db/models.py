from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race, on_delete=models.CASCADE, related_name="skill_set" # Do not add a related_name attribute here or it must be "skill_set" exactly
    )


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race, on_delete=models.CASCADE, related_name="players"
    )
    guild = models.ForeignKey(
        Guild, on_delete=models.SET_NULL, related_name="players", blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

