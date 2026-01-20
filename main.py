import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    try:
        with open("players.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("File: 'players.json' not found.")
        return

    for person in data:
        race, created = Race.objects.get_or_create(
            name=data[person]["race"]["name"],
            description=data[person]["race"]["description"]
        )

        for skill in data[person]["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        if data[person]["guild"]:
            guild, created = Guild.objects.get_or_create(
                name=data[person]["guild"]["name"],
                description=data[person]["guild"]["description"]
            )
        else:
            guild = data[person]["guild"]

        Player.objects.get_or_create(
            nickname=person,
            email=data[person]["email"],
            bio=data[person]["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
