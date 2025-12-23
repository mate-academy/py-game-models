import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        data = json.load(f)

    for nickname, player in data.items():
        race_data = player["race"]
        race_obj, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")},
        )

        guild_obj = None
        guild_data = player.get("guild")
        if guild_data is not None:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")},
            )

        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race_obj,
                },
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player["email"],
                "bio": player["bio"],
                "race": race_obj,
                "guild": guild_obj,
            },
        )


if __name__ == "__main__":
    main()
