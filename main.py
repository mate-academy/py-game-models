import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for key, value in data.items():
        race_data = value["race"] if value["race"] else None
        race_name, _ = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"])

        skills_data = race_data["skills"]
        for skill in skills_data:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race_name)

        guild_data = value["guild"]
        Player.objects.get_or_create(
            nickname=key,
            email=value["email"],
            bio=value["bio"],
            race=race_name,
            guild=Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"])[0]
            if value["guild"] is not None else None)


if __name__ == "__main__":
    main()
