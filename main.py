import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("./players.json", "r") as players_file:
        data = json.load(players_file)

    for player_name, player_info in data.items():
        race_obj = None
        guild_obj = None

        race_data = player_info.get("race")
        if race_data:
            race_obj, _ = Race.objects.get_or_create(
                name=race_data.get("name"),
                description=race_data.get("description")
            )

            for skill in race_data.get("skills", []):
                Skill.objects.get_or_create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=race_obj
                )

        guild_data = player_info.get("guild")
        if guild_data is not None:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                description=guild_data.get("description")
            )

        Player.objects.get_or_create(
            nickname=player_name,
            race=race_obj,
            guild=guild_obj,
            bio=player_info.get("bio"),
            email=player_info.get("email")
        )


if __name__ == "__main__":
    main()
