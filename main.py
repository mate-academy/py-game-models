import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    for name, info in data.items():
        race_data = info.get("race")
        if race_data:
            race, _ = Race.objects.get_or_create(
                name=race_data["name"],
                defaults={"description": race_data["description"]},
            )

        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                race=race,
                defaults={"bonus": skill_data.get("bonus")},

            )
        guild = None
        guild_data = info.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]},
            )

        Player.objects.get_or_create(
            nickname=name,
            defaults={
                "email": info["email"],
                "bio": info["bio"],
                "race": race,
                "guild": guild,
            },
        )


if __name__ == "__main__":
    main()
