import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, info in data.items():
        if not Race.objects.filter(name=info["race"]["name"]).exists():
            race = Race.objects.create(
                name=info["race"]["name"],
                description=info["race"]["description"]
            )
        race = Race.objects.get(name=info["race"]["name"])
        for skill in info["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )
        if info["guild"]:
            if not Guild.objects.filter(name=info["guild"]["name"]).exists():
                Guild.objects.create(
                    name=info["guild"]["name"],
                    description=info["guild"]["description"],
                )

            guild = Guild.objects.get(name=info["guild"]["name"])

        else:
            guild = None

        if not Player.objects.filter(nickname=nickname).exists():
            Player.objects.create(
                nickname=nickname,
                email=info["email"],
                bio=info["bio"],
                race=race,
                guild=guild,
            )


if __name__ == "__main__":
    main()
