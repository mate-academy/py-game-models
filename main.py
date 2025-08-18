import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("./players.json", "r") as f:
        players = json.load(f)
    for player in players:
        Player.objects.create(
            nickname=player,
            email=player["email"],
            bio=player["bio"],
            race=Race.objects.get_or_create(
                name=player["race"]["name"],
                description=player["race"]["description"]
            ),
            guild=Guild.objects.get_or_create(
                name=player["guild"]["name"],
                description=player["guild"]["description"]
            )
        )


if __name__ == "__main__":
    main()
