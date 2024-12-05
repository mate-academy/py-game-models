import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_info:
        players = json.load(players_info)
    for player_name, data in players.items():
        race, _ = Race.objects.get_or_create(
            name=data["race"]["name"],
            description=data["race"]["description"],
        )
        for skill in data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )
        guild = None
        guild_info = data["guild"] if data["guild"] else None
        if guild_info:
            guild, _ = Guild.objects.get_or_create(
                name=guild_info["name"],
                description=guild_info["description"],
            )
        Player.objects.get_or_create(
            nickname=player_name,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
