import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as json_file:
        players = json.load(json_file)
        for nickname, player_data in players.items():
            race_obj, created_race = Race.objects.get_or_create(
                name=player_data["race"]["name"],
                defaults={
                    "description": player_data["race"]["description"]
                }
            )
            for skill in player_data["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    race=race_obj,
                    defaults={
                        "bonus": skill["bonus"]
                    }
                )
            guild_obj = None
            if player_data["guild"]:
                guild_obj, created_guild = Guild.objects.get_or_create(
                    name=player_data["guild"]["name"],
                    defaults={
                        "description": player_data["guild"]["description"]
                    }
                )
            Player.objects.get_or_create(
                nickname=nickname,
                defaults={
                    "email": player_data["email"],
                    "bio": player_data["bio"],
                    "race": race_obj,
                    "guild": guild_obj
                }
            )


if __name__ == "__main__":
    main()
