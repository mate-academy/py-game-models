import json
from pathlib import Path

import init_django_orm  # noqa: F401
from db.models import Guild, Player, Race, Skill

BASE_DIR = Path(__file__).parent
FILE_NAME = BASE_DIR / "players.json"


def make_race(race: dict) -> Race:
    race_obj, _ = Race.objects.get_or_create(
        name=race["name"],
        defaults={"description": race.get("description", "")},
    )
    for skill in race.get("skills", []):
        Skill.objects.get_or_create(
            name=skill["name"],
            defaults={"bonus": skill.get("bonus"), "race": race_obj},
        )
    return race_obj


def make_guild(guild: dict) -> Guild | None:
    if not guild:
        return None
    guild_obj, _ = Guild.objects.get_or_create(
        name=guild["name"],
        defaults={"description": guild.get("description", "")},
    )
    return guild_obj


def main() -> None:
    with open(FILE_NAME) as file:
        data: dict = json.load(file)

    for name, players_data in data.items():
        Player.objects.get_or_create(
            nickname=name,
            defaults={
                "email": players_data["email"],
                "bio": players_data["bio"],
                "race": make_race(players_data["race"]),
                "guild": make_guild(players_data["guild"]),
            },
        )


if __name__ == "__main__":
    main()
