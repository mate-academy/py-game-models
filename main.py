import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        file_data = json.load(file)

    for name, info in file_data.items():

        Player.objects.create(
            nickname=name,
            email=info["email"],
            bio=info["bio"],
            race=Race.objects.get_or_create(
                name=info["race"]["name"],
                description=info["race"]["description"]
            )[0],
            guild=(
                Guild.objects.get_or_create(
                    name=info["guild"]["name"],
                    description=info["guild"]["description"]
                )[0]
                if info["guild"] else None
            )
        )

        for skill in info["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=Race.objects.get(name=info["race"]["name"])
            )


if __name__ == "__main__":
    main()
