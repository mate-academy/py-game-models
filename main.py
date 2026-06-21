import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, player_data in players.items():

        guild_name = player_data.get("guild")

        if guild_name:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_name.get("name"),
                defaults={
                    "description": guild_name.get("description")
                }
            )
        else:
            guild_obj = None

        race_name = player_data.get("race")

        if race_name:
            race_obj, _ = Race.objects.get_or_create(
                name=race_name.get("name"),
                defaults={
                    "description": race_name.get("description")
                }
            )
        else:
            race_obj = None

        skill_list = race_name.get("skills", []) if race_name else []
        for skill in skill_list:
            skill_obj, _ = Skill.objects.get_or_create(
                name=skill.get("name"),
                race=race_obj,
                defaults={
                    "bonus": skill.get("bonus"),
                }
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data.get("email"),
                "bio": player_data.get("bio"),
                "race": race_obj,
                "guild": guild_obj}
        )


if __name__ == "__main__":
    main()
