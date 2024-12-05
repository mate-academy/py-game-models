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
            guild_obj, created = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )
        race_obj, created = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )
        if race["skills"]:
            for skill in race["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_obj
                )
        obj = Player(
            nickname=name,
            email=value["email"],
            bio=value["bio"],
            race=race_obj,
            guild=guild_obj if guild is not None else None
        )
        obj.save()


if __name__ == "__main__":
    main()
