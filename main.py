import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as f:
        data = json.load(f)
    players = data

    for person, data in players.items():

        race, create = Race.objects.get_or_create(
            name=data["race"]["name"],
            description=data["race"]["description"]
        )

        for skill_data in data["race"]["skills"]:
            skill, create = Skill.objects.get_or_create( # noqa
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race)

        guild = data.get("guild", None)

        if guild:
            guild, create = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )

        Player.objects.create(
            nickname=person,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild
        )
