import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        players = json.load(f)

    for key, value in players.items():
        if not Race.objects.filter(name=value["race"]["name"]).exists():
            Race.objects.create(
                name=value["race"]["name"],
                description=value["race"]["description"]
            )

            for skill in value["race"]["skills"]:
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(name=value["race"]["name"])
                )

        if (
            value["guild"]
            and not Guild.objects.filter(
                name=value["guild"]["name"]
            ).exists()
        ):
            Guild.objects.create(
                name=value["guild"]["name"],
                description=value["guild"]["description"]
            )

        Player.objects.create(
            nickname=key,
            email=value["email"],
            bio=value["bio"],
            race=Race.objects.get(name=value["race"]["name"]),
            guild=(
                Guild.objects.get(name=value["guild"]["name"])
                if value["guild"]
                else None
            )
        )


if __name__ == "__main__":
    main()
