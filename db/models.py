from django.db import models


class Race(models.Model):
    """
    Represents a race entity with a name and a description.

    This model defines the core representation of a race, which includes its
    name and optional description. It is stored in a relational database and
    designed to be unique based on the `name` field.

    :ivar name: The name of the race. It is required and must be unique.
    :type name: models.CharField
    :ivar description: An optional textual description of the race.
    :type description: models.TextField
    """
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Skill(models.Model):
    """
    Represents a skill associated with a specific race.

    This class encapsulates details about a skill, including its name,
    an associated bonus, and the linkage to a specific race. The purpose
    of this class is to manage individual skills and their relationships
    to races within the system.

    :ivar name: The name of the skill. It must be unique and not exceed
        255 characters.
    :type name: models.CharField
    :ivar bonus: The bonus associated with the skill, described as a string.
        It is stored in a field with a maximum length of 255 characters.
    :type bonus: models.CharField
    :ivar race: The race associated with the skill. This is a foreign key
        pointing to the `Race` model, establishing a many-to-one relationship.
    :type race: models.ForeignKey
    """
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="skills"
    )

    def __str__(self) -> str:
        return self.name


class Guild(models.Model):
    """
    Represents a Guild entity with a name and an optional description.

    This class is used to define a guild with fields for storing its
    name and a detailed description. Intended for use in systems where
    guild-like entities are managed and require unique identification by name.

    :ivar name: The name of the guild, which is unique.
    :type name: str
    :ivar description: An optional description providing additional
        details about the guild.
    :type description: str or None
    """
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return self.name


class Player(models.Model):
    """
    Represents a player within the game.

    This class is responsible for storing player-related information such as
    their nickname, email, bio, associated race, guild, and the timestamp when
    the player was created. It serves as a model representation for players
    in the database and is linked to other models like Race and Guild.

    :ivar nickname: The unique nickname of the player.
    :type nickname: str
    :ivar email: The email address of the player.
    :type email: str
    :ivar bio: A short biography or description of the player.
    :type bio: str
    :ivar race: The race associated with the player. This is a foreign key that
        creates a relationship with the Race model.
    :type race: Race
    :ivar guild: The guild associated with the player. This is an optional
        foreign key creating a relationship with the Guild model. Can be null.
    :type guild: Guild or None
    :ivar created_at: The timestamp indicating when the player was created.
    :type created_at: datetime.datetime
    """
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="players"
    )
    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,
        null=True,
        related_name="players"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nickname
