import json
from typing import Any

import init_django_orm  # noqa: F401
from db.models import Guild, Player, Race, Skill


def main() -> None:
    with open("players.json", "r") as f:
        data: dict[str, Any] = json.load(f)

    for username, player_data in data.items():
        race_data: dict[str, Any] = player_data["race"]
        race: Race
        created: bool

        race, created = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]},
        )

        for skill_data in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race,
                },
            )

        guild_data: dict[str, Any] | None = player_data["guild"]
        guild: Guild | None = None

        if guild_data is not None:
            guild, created = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]},
            )

        Player.objects.create(
            nickname=username,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild,
        )

    print(Player.objects.count(), "players total")


if __name__ == "__main__":
    main()
