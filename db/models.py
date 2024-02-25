from django.db.models import (
    Model,
    CharField,
    TextField,
    ForeignKey,
    DateTimeField,
    EmailField,
    CASCADE,
    SET_NULL
)


class Race(Model):
    name = CharField(max_length=255, unique=True)
    description = TextField(blank=True)


class Skill(Model):
    name = CharField(max_length=255, unique=True)
    bonus = CharField(max_length=255)
    race = ForeignKey(Race, on_delete=CASCADE)


class Guild(Model):
    name = CharField(max_length=255, unique=True)
    description = TextField(null=True)


class Player(Model):
    nickname = CharField(max_length=255, unique=True)
    email = EmailField(max_length=255)
    bio = CharField(max_length=255)
    race = ForeignKey(Race, on_delete=CASCADE)
    guild = ForeignKey(Guild, null=True, on_delete=SET_NULL)
    created_at = DateTimeField(auto_now_add=True)
