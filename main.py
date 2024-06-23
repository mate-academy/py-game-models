import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_info = json.load(file)

    for nick, info in players_info.items():
        race_info = info["race"]
        guild_info = info["guild"]

        race_data, _ = Race.objects.get_or_create(
            name=race_info["name"],
            description=race_info["description"])

        guild_data = None
        if guild_info:
            guild_data, _ = Guild.objects.get_or_create(
                name=guild_info["name"],
                description=guild_info["description"])

        for skill in race_info["skills"]:
            Skill.objects.get_or_create(name=skill["name"],
                                        bonus=skill["bonus"],
                                        race=race_data)

        Player.objects.create(
            nickname=nick,
            email=info["email"],
            bio=info["bio"],
            race=race_data,
            guild=guild_data
        )
