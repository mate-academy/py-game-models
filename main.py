import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json") as file:
        players = json.load(file)

    for player_name, player_data in players.items():

        player_race, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            defaults={
                "description": player_data["race"].get("description", "")
            }
        )

        if "skills" in player_data["race"]:
            for skill in player_data["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    defaults={
                        "bonus": skill["bonus"],
                        "race": player_race
                    }
                )

        player_guild = None

        if "guild" in player_data and player_data["guild"]:
            player_guild, _ = Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                defaults={
                    "description": player_data["guild"].get("description", "")
                }
            )

        Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": player_race,
                "guild": player_guild
            }
        )


if __name__ == "__main__":
    main()
