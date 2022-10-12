import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file_json:
        info_players = json.load(file_json)
        for player_name in info_players:

            if Race.objects.filter(
                    name=info_players[player_name]["race"]["name"],
                    description=info_players[player_name]["race"]["description"]
            ).exists() is False:
                Race.objects.create(
                    name=info_players[player_name]["race"]["name"],
                    description=info_players[player_name]["race"]["description"]
                )

            if not info_players[player_name]["guild"]:
                guild_name = None
            else:
                if Guild.objects.filter(
                    name=info_players[player_name]["guild"]["name"],
                    description=info_players[player_name]["guild"]["description"]
                ).exists() is False:
                    guild_name = Guild.objects.create(
                        name=info_players[player_name]["guild"]["name"],
                        description=info_players[player_name]["guild"]["description"]
                    )

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

            if not guild_name:
                Player.objects.create(
                    nickname=player_name,
                    email=info_players[player_name]["email"],
                    bio=info_players[player_name]["bio"],
                    race=Race.objects.get(
                        name=info_players[player_name]["race"]["name"]
                    ),
                    guild=None
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
                            name=info_players[player_name]["guild"]["name"]
                    )
                )


if __name__ == "__main__":
    main()
