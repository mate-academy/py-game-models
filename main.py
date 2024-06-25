import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

        for player_name, player_info in players_data.items():
            race_name = player_info["race"]["name"]
            race_description = player_info["race"]["description"]
            race_obj, _ = Race.objects.get_or_create(
                name=race_name,
                defaults={
                    "description": race_description
                }
            )

            guild_info = player_info.get("guild")
            if guild_info:
                guild_name = guild_info["name"]
                guild_description = guild_info.get("description", "")
                guild_obj, _ = Guild.objects.get_or_create(
                    name=guild_name,
                    defaults={
                        "description": guild_description
                    }
                )
            else:
                guild_obj = None

            player_obj, _ = Player.objects.get_or_create(
                nickname=player_name,
                defaults={
                    "email": player_info["email"],
                    "bio": player_info["bio"],
                    "race": race_obj,
                    "guild": guild_obj
                }
            )

            for skill in player_info["race"]["skills"]:
                skill_name = skill["name"]
                skill_bonus = skill["bonus"]
                Skill.objects.get_or_create(
                    name=skill_name,
                    defaults={
                        "bonus": skill_bonus,
                        "race": race_obj
                    }
                )


if __name__ == "__main__":
    main()
