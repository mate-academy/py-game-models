import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json") as pj:
        game_data = json.load(pj)

    player_race = Race.objects.create(
        name=game_data["john"]["race"]["name"],
        description=game_data["john"]["race"]["description"]
    )

    new_guild = Guild.objects.create(
        name=game_data["max"]["guild"]["name"],
        description=game_data["max"]["guild"]["description"]
    )
    for key, value in game_data.items():
        if key == "arthur":
            for key1, values in value.items():
                if key1 == "race":
                    Skill.objects.create(
                        name=values["skills"][0]["name"],
                        bonus=values["skills"][0]["bonus"],
                        race=player_race
                    )

    Player.objects.create(
        nickname="andrew",
        email=game_data["andrew"]["email"],
        race=player_race,
        guild=new_guild
    )


if __name__ == "__main__":
    main()
