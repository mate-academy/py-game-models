import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json", "r") as players_file:
        players = json.load(players_file)

    for player in players:
        if not Race.objects.filter(
                name=players[player]["race"]["name"]
        ).exists():
            Race.objects.create(
                name=players[player]["race"]["name"],
                description=players[player]["race"]["description"]

            )

        for skill in players[player]["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(
                        name=players[player]["race"]["name"]
                    )
                )
        if players[player]["guild"] is not None:
            if not Guild.objects.filter(
                    name=players[player]["guild"]["name"]
            ).exists() and players[player]["guild"] is not None:
                Guild.objects.create(
                    name=players[player]["guild"]["name"],
                    description=players[player]["guild"]["description"]

                )

            Player.objects.create(
                nickname=player,
                email=players[player]["email"],
                bio=players[player]["bio"],
                race=Race.objects.get(name=players[player]["race"]["name"]),
                guild=Guild.objects.get(name=players[player]["guild"]["name"])
            )
        else:
            Player.objects.create(
                nickname=player,
                email=players[player]["email"],
                bio=players[player]["bio"],
                race=Race.objects.get(name=players[player]["race"]["name"]),
            )


if __name__ == "__main__":
    main()
