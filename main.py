import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json") as players:
        data = json.load(players)
    list_of_race = []
    for name, info in data.items():
        name_of_race = info["race"]["name"]
        if name_of_race not in list_of_race:
            list_of_race.append(name_of_race)
            Race.objects.create(
                name=name_of_race,
                description=info["race"]["description"]
            )

    skills = list(data.values())[1]["race"]["skills"]
    for skill in skills:
        Skill.objects.create(
            name=skill["name"],
            bonus=skill["bonus"],
            race=Race.objects.get(name="elf")
        )

    list_of_guils = []
    for name, info in data.items():
        guild = info["guild"]
        if isinstance(guild, dict) and\
                guild["name"] not in list_of_guils:
            list_of_guils.append(guild["name"])
            Guild.objects.create(
                name=guild["name"],
                description=guild["description"]
            )
    for name, info in data.items():
        name_of_race = info["race"]["name"]
        if info["guild"] is not None:
            Player.objects.create(
                nickname=name,
                email=info["email"],
                bio=info["bio"],
                race=Race.objects.get(name=name_of_race),
                guild=Guild.objects.get(name=info["guild"]["name"])
            )
        else:
            Player.objects.create(
                nickname=name,
                email=info["email"],
                bio=info["bio"],
                race=Race.objects.get(name=name_of_race)
            )


if __name__ == "__main__":
    main()
