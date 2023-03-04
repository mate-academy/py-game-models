import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json") as pj:
        game_data = json.load(pj)

    list_of_name = list(game_data)

    player_race = Race.objects.create(
        name=game_data[str(list_of_name[0])]["race"]["name"],
        description=game_data[str(list_of_name[0])]["race"]["description"]
    )

    new_guild = Guild.objects.create(
        name=game_data[str(list_of_name[1])]["guild"]["name"],
        description=game_data[str(list_of_name[1])]["guild"]["description"]
    )
    for key, value in game_data.items():
        if key == str(list_of_name[2]):
            for key1, values in value.items():
                if key1 == "race":
                    Skill.objects.create(
                        name=values["skills"][0]["name"],
                        bonus=values["skills"][0]["bonus"],
                        race=player_race
                    )

    Player.objects.create(
        nickname=str(list_of_name[3]),
        email=game_data[str(list_of_name[3])]["email"],
        bio=game_data[str(list_of_name[3])]["bio"],
        race=player_race,
        guild=new_guild
    )


if __name__ == "__main__":
    main()
