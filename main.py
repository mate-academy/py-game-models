import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_name, player_info in players_data.items():
        race_info = player_info.get("race")
        if race_info:
            race_name = race_info.get("name")
            race_description = race_info.get("description")
            race, _ = Race.objects.get_or_create(
                name=race_name,
                defaults={"description": race_description}
            )

            skills = race_info.get("skills", [])
            for skill_info in skills:
                skill_name = skill_info.get("name")
                skill_bonus = skill_info.get("bonus")
                if skill_name and skill_bonus:
                    Skill.objects.get_or_create(
                        name=skill_name,
                        bonus=skill_bonus,
                        race=race  # Прив'язка до раси
                    )

        guild_info = player_info.get("guild")
        guild = None
        if guild_info:
            guild_name = guild_info.get("name")
            guild_description = guild_info.get("description")
            if guild_name:
                guild, _ = Guild.objects.get_or_create(
                    name=guild_name,
                    defaults={"description": guild_description}
                )

        Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": player_info.get("email"),
                "bio": player_info.get("bio"),
                "race": race,
                "guild": guild
            }
        )



if __name__ == "__main__":
    main()
