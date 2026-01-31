import json

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, player_info in players.items():
        race_info = player_info.get("race")
        guild_info = player_info.get("guild")
        skills_info = race_info.get("skills")

        race, is_race_created = Race.objects.get_or_create(
            name=race_info.get("name"),
            defaults={
                "description": race_info.get("description")
            }
        )

        if is_race_created:
            for el in skills_info:
                skills, _ = Skill.objects.get_or_create(
                    name=el.get("name"),
                    race=race,
                    defaults={
                        "bonus": el.get("bonus")
                    }
                )
        if guild_info is not None:
            guild, _ = Guild.objects.get_or_create(
                name=guild_info.get("name"),
                defaults={
                    "description": guild_info.get("description")
                }
            )
        else:
            guild = None

        Player.objects.create(
            nickname=nickname,
            email=player_info.get("email"),
            bio=player_info.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
