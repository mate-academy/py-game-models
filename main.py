import init_django_orm  # noqa: F401

import json

from typing import Any

from db.models import Race, Skill, Player, Guild


def get_data() -> dict[str, Any]:
    try:
        with open("players.json", "r") as p_file:
            return json.load(p_file)
    except FileNotFoundError as e:
        raise SystemExit(f"File not found: {e}")


def main() -> None:
    data = get_data()

    for nickname, value in data.items():
        email = value["email"]
        bio = value["bio"]

        guild_data = value.get("guild")
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]}
            )

        race_data = value["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]}
        )

        skills = race_data.get("skills", [])
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                race=race,
                defaults={"bonus": skill["bonus"]}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": email,
                "bio": bio,
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
