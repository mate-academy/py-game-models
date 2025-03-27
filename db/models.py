from django.db import models as m


class Race(m.Model):
    name = m.CharField(unique=True, max_length=255)
    description = m.TextField(blank=True)


class Skill(m.Model):
    name = m.CharField(unique=True, max_length=255)
    bonus = m.CharField(max_length=255)
    race = m.ForeignKey(Race, on_delete=m.CASCADE)


class Guild(m.Model):
    name = m.CharField(unique=True, max_length=255)
    description = m.TextField(null=True)


class Player(m.Model):
    nickname = m.CharField(unique=True, max_length=255)
    email = m.EmailField(max_length=255)
    bio = m.CharField(max_length=255)
    race = m.ForeignKey(Race, on_delete=m.CASCADE)
    guild = m.ForeignKey(Guild, on_delete=m.SET_NULL, null=True)
    created_at = m.DateTimeField(auto_now_add=True)
