import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        data = json.load(players_file)

    for key, value in data.items():
        race_obj, created = Race.objects.get_or_create(
            name=value["race"]["name"],
            description=value["race"]["description"]
        )

        skills_list = value["race"]["skills"]
        if skills_list:
            for skill in skills_list:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_obj
                )

        guild_data = value.get("guild")
        guild_obj = None
        if guild_data:
            guild_obj, created = Guild.objects.get_or_create(
                name=value["guild"]["name"],
                description=value["guild"]["description"]
            )

        Player.objects.create(
            nickname=key,
            email=value["email"],
            bio=value["bio"],
            race=race_obj,
            guild=guild_obj
        )


if __name__ == "__main__":
    main()
