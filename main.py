import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file_json:
        info_players = json.load(file_json)
        for player_name in info_players:

            #Race
            if Race.objects.filter(
                    name=info_players[player_name]["race"]["name"],
                    description=info_players[player_name]["race"]["description"]
            ).exists() is False:
                Race.objects.create(
                    name=info_players[player_name]["race"]["name"],
                    description=info_players[player_name]["race"]["description"]
                )

            #Guild
            # if Guild.objects.get(name=info_players[player_name]["guild"]) is None:
            #     Guild.objects.create(
            #         name=None,
            #         description=info_players[player_name]["guild"]["description"]
            #     )

            if Guild.objects.filter(
                    name=info_players[player_name]["guild"]["name"],
                    description=info_players[player_name]["guild"]["description"]
            ).exists() is False:
                Guild.objects.create(
                    name=info_players[player_name]["guild"]["name"],
                    description=info_players[player_name]["guild"]["description"]
                )

            #Skills

            for single_skill in info_players[player_name]["race"]["skills"]:
                if Skill.objects.filter(
                    name=single_skill["name"], bonus=single_skill["bonus"]
                ).exists() is False:
                    Skill.objects.create(
                        name=single_skill["name"],
                        bonus=single_skill["bonus"],
                        race=Race.objects.get(
                            name=info_players[player_name]["race"]["name"]
                        )
                    )


            #Create a Player
            if Guild.objects.get(name=info_players[player_name]["guild"]) is not None:
                Player.objects.create(
                    nickname=player_name,
                    email=info_players[player_name]["email"],
                    bio=info_players[player_name]["bio"],
                    race=Race.objects.get(
                        name=info_players[player_name]["race"]["name"]
                    ),
                    guild=Guild.objects.get(
                        name=info_players[player_name]["guild"]["name"]
                    )
                )
            else:
                Player.objects.create(
                    nickname=player_name,
                    email=info_players[player_name]["email"],
                    bio=info_players[player_name]["bio"],
                    race=Race.objects.get(
                        name=info_players[player_name]["race"]["name"]
                    ),
                    guild=Guild.objects.get(
                        name=None
                    )
                )


if __name__ == "__main__":
    main()
