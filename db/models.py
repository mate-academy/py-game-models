from django.db import models


class Race(models.Model):
    RACES = (
        ("elf", "Elf"),
        ("dwarf", "Dwarf"),
        ("human", "Human"),
        ("ork", "Ork")
    )
    name = models.CharField(max_length=255, choices=RACES, unique=True)
    description = models.TextField(blank=True)
