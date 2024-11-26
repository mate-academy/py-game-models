import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        players = json.load(f)

    for nickname, info in players.items():
        race = None
        if not Race.objects.filter(name=info["race"]["name"]).exists():
            race = Race.objects.create(
                name=info["race"]["name"],
                description=info["race"]["description"]
            )

            for skill in info["race"]["skills"]:
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        if (
            info["guild"]
            and not Guild.objects.filter(
                name=info["guild"]["name"]
            ).exists()
        ):
            Guild.objects.create(
                name=info["guild"]["name"],
                description=info["guild"]["description"]
            )

        Player.objects.create(
            nickname=nickname,
            email=info["email"],
            bio=info["bio"],
            race=race if race else Race.objects.get(name=info["race"]["name"]),
            guild=(
                Guild.objects.get(name=info["guild"]["name"])
                if info["guild"]
                else None
            )
        )


if __name__ == "__main__":
    main()
