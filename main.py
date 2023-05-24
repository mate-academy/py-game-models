import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)
    for player, data in players.items():
        race_data = data["race"] if data["race"] else None
        race = Race.objects.create(
            name=race_data["name"],
            description=race_data["description"]
        )

        skills_data = data["race"]["skills"] if data["race"]["skills"] else None
        Skill.objects.create(
            name=skills_data["name"],
            bonus=skills_data["bonus"],
            race=race
        )

        guild_data = data["guild"] if data["guild"] else None
        guild = Guild.objects.create(
            name=guild_data["name"],
            description=guild_data["description"]
        )

        Player.objects.create(
            nickname=players["nickname"],
            email=players["email"],
            bio=players["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
