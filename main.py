import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player_nickname, player_data in data.items():
        race_data = player_data.get("race")
        race_name = race_data.get("name")
        race_description = race_data.get("description")
        race_skills = race_data.get("skills")
        race_object = Race.objects.get_or_create(
            name=race_name,
            defaults={
                "name": race_name,
                "description": race_description
            }
        )[0]
        if race_skills:
            for skill in race_skills:
                skill_name = skill.get("name")
                skill_bonus = skill.get("bonus")
                Skill.objects.get_or_create(
                    name=skill_name,
                    defaults={
                        "name": skill_name,
                        "bonus": skill_bonus,
                        "race": race_object
                    }
                )

        guild_data = player_data.get("guild")

        Player.objects.create(
            nickname=player_nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race_object,
            guild=Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults=guild_data
            )[0]
            if guild_data
            else None
        )


if __name__ == "__main__":
    main()
