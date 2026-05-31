import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as f:
        players = json.load(f)

    for player, data in players.items():

        race, create = Race.objects.get_or_create(
            name=data["race"]["name"],
            description=data["race"]["description"]
        )

        for skill_data in data["race"]["skills"]:
            skill, create = Skill.objects.get_or_create( # noqa
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race)

        guild_data = data.get("guild", None)

        if guild_data:
            guild, create = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
            )
        else:
            guild = None

        Player.objects.create(
            nickname=player,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild if guild_data else None,
        )
