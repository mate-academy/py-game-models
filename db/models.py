"""
Create the following models:

1. Race

    Each player should choose a race to play, such as Elf, Dwarf, Human, or
    Ork. Race has the following fields:

    - name - a unique char field with the maximum length of 255 characters.
    - description - a text field, can be blank.

2. Skill

    Each race has unique skills. Create a model Skill for them. Each skill has:

    - name - a unique char field with a maximum length of 255 characters.
    - bonus - a char field with a maximum length of 255 characters. This field
        describes what kind of bonus players can get from it. In other words,
        this is a description of the bonus.
    - race - a foreign key that points to the Race model. It shows which race
        has the corresponding skill. Important Note: The skill must be deleted
        when the race is deleted.

3. Guild

    The player has an opportunity to become a member of a guild. It has:

    - name - a unique char field with the maximum length of 255 characters.
    - description - a text field, can be null.

4. Player model

    And finally, a Player model. It should have the following fields:

    - nickname - a unique char field with a maximum length of 255 characters.
    - email - an email field with a maximum length of 255 characters. It can
        be non-unique.
    - bio - a CharField with a maximum length of 255 characters. It stores a
        short description provided by a user about himself/herself.
    - race - a foreign key that points to the Race model and shows the race of
        the player. Important Note: The player must be deleted when the race
        is deleted.
    - guild - a foreign key that points to the Guild model and stores an id of
        the guild the player is a member of. Please note: player should not be
        deleted when the guild is deleted.
    - created_at - a DateTime field, that is set with the current time by
        default.
"""

from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE
    )


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="player_race"
    )
    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="player_guild")
    created_at = models.DateTimeField(auto_now_add=True)
