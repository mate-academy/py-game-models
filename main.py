import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, info in data.items():
        race_data = info.get("race", {})
        race_obj, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={"description": race_data.get("description", "")}
        )

        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data.get("name"),
                race=race_obj,
                defaults={"bonus": skill_data.get("bonus", "")}
            )

        guild_data = info.get("guild")
        guild_obj = None
        if guild_data:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": info.get("email"),
                "bio": info.get("bio", ""),
                "race": race_obj,
                "guild": guild_obj
            }
        )


if __name__ == "__main__":
    main()
