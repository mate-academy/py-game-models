from django.db.models import (
    Model,
    CharField,
    TextField,
    EmailField,
    ForeignKey,
    DateTimeField,
    CASCADE,
    SET_NULL
)


class Race(Model):
    name = CharField(max_length=255, unique=True)
    description = TextField(blank=True)

    def __str__(self) -> CharField:
        return self.name


class Skill(Model):
    name = CharField(max_length=255, unique=True)
    bonus = CharField(max_length=255)
    race = ForeignKey(Race, on_delete=CASCADE)

    def __str__(self) -> CharField:
        return self.name


class Guild(Model):
    name = CharField(max_length=255, unique=True)
    description = TextField(null=True)

    def __str__(self) -> CharField:
        return self.name


class Player(Model):
    nickname = CharField(max_length=255, unique=True)
    email = EmailField(max_length=255)
    bio = CharField(max_length=255)
    race = ForeignKey(Race, on_delete=CASCADE)
    guild = ForeignKey(Guild, on_delete=SET_NULL, null=True)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self) -> CharField:
        return self.nickname
