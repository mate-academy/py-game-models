import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


JSON_FILE = "players.json"


def main() -> None:
    with open(JSON_FILE, "r") as file:
        players = json.load(file)

    for name, data in players.items():
        race_dict = data["race"]

        race, cr = Race.objects.get_or_create(
            name=race_dict["name"],
            description=race_dict["description"]
        )
        race = Race.objects.get(name=race_dict["name"])

        for skill in race_dict["skills"]:

            skill, cr = Skill.objects.get_or_create(
                name=skill["name"], bonus=skill["bonus"], race=race
            )

        guild = data["guild"] if data["guild"] else None
        if guild:
            guild, cr = Guild.objects.get_or_create(
                name=data["guild"]["name"],
                description=data["guild"]["description"]
            )

        Player.objects.create(
            nickname=name,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
