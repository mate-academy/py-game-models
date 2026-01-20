import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as json_players_file:
        players = json.load(json_players_file)

    if players:
        for name, player in players.items():
            player_race = Race.get_or_create(player["race"])
            player_guild = Guild.get_or_create(player["guild"])

            for skill in player["race"]["skills"]:
                Skill.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=player_race
                )

            Player.objects.create(
                nickname=name,
                email=player["email"],
                bio=player["bio"],
                race=player_race,
                guild=player_guild
            )


if __name__ == "__main__":
    main()
