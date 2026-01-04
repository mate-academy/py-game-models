import json

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    for nickname, player_data in data.items():
        race_info = player_data.get("race")
        race_name = race_info.get("name")
        race_desc = race_info.get("description")
        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_desc or ""}
        )
        skills = race_info.get("skills")

        if skills is None:
            continue

        for skill_data in skills:
            Skill.objects.get_or_create(
                name=skill_data.get("name"),
                defaults={
                    "bonus": skill_data.get("bonus", ""),
                    "race": race
                }
            )
        guild_info = player_data.get("guild")
        guild_obj = None

        if guild_info:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_info.get("name"),
                defaults={"description": guild_info.get("description")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data.get("email"),
                "bio": player_data.get("bio"),
                "race": race,
                "guild": guild_obj,
            }
        )


if __name__ == "__main__":
    main()
