import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_dict = json.load(file)

    for player_name, player_info in players_dict.items():

        player_guild = None

        if player_info["guild"] is not None:
            if not Guild.objects.filter(
                    name=player_info["guild"]["name"]).exists():
                player_guild = Guild.objects.create(
                    name=player_info["guild"]["name"],
                    description=player_info["guild"]["description"]
                )
            else:
                player_guild = \
                    Guild.objects.get(name=player_info["guild"]["name"])

        if not Race.objects.filter(
                name=player_info["race"]["name"]).exists():
            player_race = Race.objects.create(
                name=player_info["race"]["name"],
                description=player_info["race"]["description"],
            )
            for skill in player_info["race"]["skills"]:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=player_race,
                    )
        else:
            player_race = \
                Race.objects.get(name=player_info["race"]["name"])

        Player.objects.create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=player_race,
            guild=player_guild
        )


if __name__ == "__main__":
    main()
