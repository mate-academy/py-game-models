from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(
        max_length=255,
        help_text="""
        This field describes what kind of bonus players can get from it. In
         other words, this is a description of the bonus
        """
    )
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="skills"
    )


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=False)
    bio = models.CharField(
        max_length=255,
        help_text="""
        It stores a short description provided by a user about himself/herself
        """
    )
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="players"
    )
    guild = models.ForeignKey(
        Guild,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="players"
    )
    created_at = models.DateTimeField(auto_now_add=True)
