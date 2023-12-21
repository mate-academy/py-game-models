import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players:
        players_data = json.load(players)
        for player_name in players_data:
            player = players_data[f"{player_name}"]
            Race.objects.get_or_create(
                name=player["race"]["name"],
                description=player["race"]["description"]
            )

            for skill in range(len(player["race"]["skills"])):
                Skill.objects.get_or_create(
                    name=player["race"]["skills"][skill]["name"],
                    bonus=player["race"]["skills"][skill]["bonus"],
                    race=Race.objects.get_or_create(
                        name=player["race"]["name"]
                    ).id
                )

            Guild.objects.get_or_create(
                name=player["guild"]["name"],
                description=player["guild"]["description"]
            )

            Player.objects.get_or_create(
                nickname=player,
                email=player["email"],
                bio=player["bio"],
                race=Race.objects.get_or_create(
                    name=player["race"]["name"]
                ).id,
                guild=Guild.objects.get_or_create(
                    name=player["guild"]["name"]
                ).id,
            )


if __name__ == "__main__":
    main()
