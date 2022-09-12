from django.db import models


class Race(models.Model):
    """Each player should choose a race to play,
    such as Elf, Dwarf, Human, or Ork."""
    name = models.CharField(max_length=255,
                            unique=True)
    description = models.TextField(blank=True)


class Skill(models.Model):
    """Each race has unique skills.
    Create a model Skill for them."""
    name = models.CharField(max_length=255,
                            unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race,
                             on_delete=models.CASCADE,
                             null=True)


class Guild(models.Model):
    """ The player has an opportunity
    to become a member of a guild. """
    name = models.CharField(max_length=255,
                            unique=True)
    description = models.TextField(blank=True,
                                   null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255,
                                unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(Race,
                             on_delete=models.SET_NULL,
                             null=True)
    guild = models.ForeignKey(Guild,
                              on_delete=models.CASCADE,
                              null=True)
    created_at = models.DateTimeField(auto_now=True)
