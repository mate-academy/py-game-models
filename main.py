import json

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player, properties in data.items():
        email = properties["email"]
        bio = properties["bio"]
        skills = properties["race"]["skills"]

        race, _ = Race.objects.get_or_create(
            name=properties["race"]["name"],
            description=properties["race"]["description"]
        )

        for skill in skills:
            if not Skill.objects.filter(name=skill["name"]):
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        player = Player(
            nickname=player,
            email=email,
            bio=bio,
            race=race
        )

        if properties["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=properties["guild"]["name"],
                description=properties["guild"]["description"]
            )
            player.guild = guild

        player.save()
