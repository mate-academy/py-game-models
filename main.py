import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as player_json:
        players = json.load(player_json)
        for player in players:
            Race.objects.get_or_create(
                name=players[player]["race"]["name"],
                description=players[player]["race"]["description"],
            )

            for skill in players[player]["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(
                        name=players[player]["race"]["name"]
                    ),
                )
            guild = None

            if players[player]["guild"] is not None:
                guild = Guild.objects.get_or_create(
                    name=players[player]["guild"]["name"],
                    description=players[player]["guild"]["description"],
                )

            Player.objects.create(
                nickname=player,
                email=players[player]["email"],
                bio=players[player]["bio"],
                race=Race.objects.get(name=players[player]["race"]["name"]),
                guild=Guild.objects.get(
                    name=players[player]["guild"]["name"]
                ) if guild else None,
            )


if __name__ == "__main__":
    main()
