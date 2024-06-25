from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    bio = models.TextField()
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)




# class Car(models.Model):
#     ENGINE_TYPE = (
#         ("ICE", "internal combustion engine"),
#         ("HYBRID", "hybrid engine"),
#         ("ELECTRICAL", "electrical engine"),
#     )
#
#     brand = models.CharField(max_length=255)
#     horse_power = models.IntegerField()
#     creation_date = models.DateField(null=True, blank=True)
#     description = models.TextField(default="It is very good car")
#     engine_type = models.CharField(max_length=20, choices=ENGINE_TYPE, null=True)
#     record_created = models.DateTimeField(null=True, auto_now=True)
#
#     def __str__(self):
#         return f"{self.id} {self.brand} (power: {self.horse_power})"
