from __future__ import annotations
from django.db import models as mod


class Race(mod.Model):
    name = mod.CharField(max_length=255, unique=True)
    description = mod.TextField(blank=True)


class Skill(mod.Model):
    name = mod.CharField(max_length=255, unique=True)
    bonus = mod.CharField(max_length=255)
    race = mod.ForeignKey("Race", on_delete=mod.CASCADE)


class Guild(mod.Model):
    name = mod.CharField(max_length=255, unique=True)
    description = mod.TextField(null=True)


class Player(mod.Model):
    nickname = mod.CharField(max_length=255, unique=True)
    email = mod.EmailField(max_length=255)
    bio = mod.CharField(max_length=255, blank=True)
    race = mod.ForeignKey("Race", on_delete=mod.CASCADE)
    guild = mod.ForeignKey("Guild", on_delete=mod.SET_NULL, null=True)
    created_at = mod.DateTimeField(auto_now=True)
