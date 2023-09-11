import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        file_data = json.load(file)

    for name, info in file_data.items():

        if not Race.objects.filter(name=info["race"]["name"]).exists():
            Race.objects.create(
                name=info["race"]["name"],
                description=info["race"]["description"]
            )

        for skill in info["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(name=info["race"]["name"])
                )

        if not info["guild"] is None:
            if not Guild.objects.filter(name=info["guild"]["name"]).exists():
                Guild.objects.create(
                    name=info["guild"]["name"],
                    description=info["guild"]["description"]
                )

        Player.objects.create(
            nickname=name,
            email=info["email"],
            bio=info["bio"],
            race=Race.objects.get(name=info["race"]["name"]),
            guild=(
                Guild.objects.get(name=info["guild"]["name"])
                if info["guild"] else None
            )
        )


if __name__ == "__main__":
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Guild.objects.all().delete()
    Player.objects.all().delete()

    main()
