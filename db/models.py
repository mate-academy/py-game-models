from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(
        max_length=255,
        help_text="Description of the bonus players receive."
    )
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="skills"
    )


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(
        max_length=255,
        help_text="Description about user"
    )
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name="players")
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True, related_name="players")
    created_at = models.DateTimeField(auto_now_add=True)
