import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as json_file:
        players_dict = json.load(json_file)

    for name, attributes in players_dict.items():
        guild = attributes.get("guild")

        if guild:
            if not Guild.objects.filter(name=guild["name"]).exists():
                Guild(
                    name=guild["name"],
                    description=guild["description"]
                ).save()
            guild = Guild.objects.get(name=guild["name"])

        race_name = attributes["race"]["name"]
        if not Race.objects.filter(name=race_name).exists():
            Race(
                name=race_name,
                description=attributes["race"]["description"]
            ).save()

        for skills in attributes["race"]["skills"]:
            print(skills)
            if not Skill.objects.filter(name=skills["name"]).exists():
                Skill(
                    name=skills["name"],
                    bonus=skills["bonus"],
                    race=Race.objects.get(name=race_name)
                ).save()

        Player(
            nickname=name,
            email=attributes["email"],
            bio=attributes["bio"],
            race=Race.objects.get(name=race_name),
            guild=guild
        ).save()


if __name__ == "__main__":
    main()
