import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as f:
        players = json.load(f)

    for nickname, info in players.items():
        race_data = info.get("race", {})
        guild_data = info.get("guild")

        race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={"description": race_data.get("description", "")},
        )

        skills_data = race_data.get("skills", [])
        for skill in skills_data:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                defaults={
                    "bonus": skill.get("bonus", ""),
                    "race": race,
                },
            )

        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description", None)},
            )

        else:
            guild = None

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": info.get("email"),
                "bio": info.get("bio", ""),
                "race": race,
                "guild": guild,
            },
        )


if __name__ == "__main__":
    main()
