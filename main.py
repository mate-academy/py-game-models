import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("./players.json", "r") as f:
        players = json.load(f)
    for player in players:
        Player.objects.create(
            nickname=player,
            email=player.get("email"),
            bio=player.get("bio"),
            race=Race.objects.get_or_create(
                name=player.get("race").get("name"),
                defaults={"description":player.get("race").get("description")}
            ),
            guild=Guild.objects.get_or_create(
                name=player.get("guild").get("name", None),
                defaults={"description":player.get("guild").get("description")}
            )
        )


if __name__ == "__main__":
    main()
