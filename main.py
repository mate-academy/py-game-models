import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        data_from_file = json.load(file)

    for player_name, values in data_from_file.items():
        email = values.get("email")
        bio = values.get("bio")

        race_info = values.get("race", {})
        race_name = race_info.get("name")
        race_desc = race_info.get("description")
        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_desc}
        )

        for skill_info in race_info.get("skills", []):
            skill_name = skill_info.get("name")
            skill_bonus = skill_info.get("bonus")
            Skill.objects.get_or_create(
                name=skill_name,
                defaults={"bonus": skill_bonus, "race": race}
            )

        guild_info = values.get("guild")
        guild_obj = None
        if guild_info:
            guild_name = guild_info.get("name")
            guild_desc = guild_info.get("description")
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_desc}
            )

        Player.objects.create(
            nickname=player_name,
            email=email,
            bio=bio,
            race=race,
            guild=guild_obj
        )


if __name__ == "__main__":
    main()
