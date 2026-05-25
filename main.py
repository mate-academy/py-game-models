import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

        for nickname, player in players.items():
            guild_data = player.get("guild")
            guild_obj = None

            if guild_data:
                guild_obj, _ = Guild.objects.get_or_create(
                    name=guild_data["name"],
                    defaults={
                        "description": guild_data.get("description", "")
                    }
                )

            race_data = player.get("race")
            race_obj, _ = Race.objects.get_or_create(
                name=race_data["name"],
                defaults={"description": race_data.get("description", "")}
            )

            player_obj, _ = Player.objects.get_or_create(
                nickname=nickname,
                email=player["email"],
                defaults={
                    "race": race_obj,
                    "guild": guild_obj,
                    "bio": player.get("bio", "")
                }
            )
            skills_data = race_data.get("skills", [])

            for skill_data in skills_data:
                Skill.objects.get_or_create(
                    name=skill_data["name"],
                    defaults={"bonus": skill_data["bonus"],
                              "race": race_obj,
                              }
                )


if __name__ == "__main__":
    main()
