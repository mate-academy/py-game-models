import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def get_race(race_data: dict) -> Race:
    race, _ = Race.objects.get_or_create(
        name=race_data["name"],
        defaults={"description": race_data.get("description", "")},
    )
    for skill in race_data.get("skills", []):
        Skill.objects.get_or_create(
            name=skill["name"],
            defaults={"bonus": skill["bonus"], "race": race},
        )
    return race


def get_guild(guild_data: dict | None) -> Guild | None:
    if not guild_data:
        return None
    guild, _ = Guild.objects.get_or_create(
        name=guild_data["name"],
        defaults={"description": guild_data.get("description")},
    )
    return guild


def main() -> None:
    with open("players.json", encoding="utf-8") as file:
        players = json.load(file)

    for nickname, data in players.items():
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": data["email"],
                "bio": data["bio"],
                "race": get_race(data["race"]),
                "guild": get_guild(data.get("guild")),
            },
        )


if __name__ == "__main__":
    main()
