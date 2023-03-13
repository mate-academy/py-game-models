import json

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild

file_name = "players.json"


def main() -> None:
    with open(file_name, "r") as file:
        players = json.load(file)

    for name, info in players.items():
        if info["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=info["guild"]["name"],
                description=info["guild"]["description"]
            )
        else:
            guild = None

        race, created = Race.objects.get_or_create(
            name=info["race"]["name"],
            description=info["race"]["description"]
        )

        if created:
            for skill in info["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"], bonus=skill["bonus"], race=race
                )

        if not Player.objects.filter(nickname=name).exists():
            Player.objects.create(
                nickname=name,
                email=info["email"],
                bio=info["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
