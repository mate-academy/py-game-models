import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as inputs:
        data = json.load(inputs)
    for name, value in data.items():
        guild = value["guild"]
        race = value["race"]
        if guild is not None:
            if not Guild.objects.filter(name=guild["name"]).exists():
                obj = Guild(
                    name=value["guild"]["name"],
                    description=value["guild"]["description"]
                )
                obj.save()
                value["guild"] = obj
            else:
                obj = Guild.objects.get(name=guild["name"])
                value["guild"] = obj
        if not Race.objects.filter(name=race["name"]).exists():
            race_obj = Race(
                name=race["name"],
                description=race["description"]
            )
            race_obj.save()
            race["name"] = race_obj
        else:
            race_obj = Race.objects.get(name=race["name"])
            race["name"] = race_obj
        if race["skills"]:
            for skill in race["skills"]:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    obj = Skill(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race_obj
                    )
                    obj.save()
    for name, value in data.items():
        obj = Player(
            nickname=name,
            email=value["email"],
            bio=value["bio"],
            race=value["race"]["name"],
            guild=value["guild"]
        )
        obj.save()


if __name__ == "__main__":
    main()
