import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_dict = json.load(file)

    for player_name, information in players_dict.items():

        race_name = information["race"]["name"]
        race_description = information["race"]["description"]
        if not Race.objects.filter(name=race_name).exists():
            Race.objects.create(
                name=race_name,
                description=race_description
            )
        for skill in information["race"]["skills"]:
            skill_name = skill["name"]
            skill_bonus = skill["bonus"]
            skill_race = Race.objects.get(name=race_name)
            if not Skill.objects.filter(name=skill_name):
                Skill.objects.create(
                    name=skill_name,
                    bonus=skill_bonus,
                    race=skill_race
                )
        guild_name = None
        if information["guild"]:
            guild_name = information["guild"].get("name")
            guild_description = information["guild"]["description"]
            if not Guild.objects.filter(name=guild_name).exists():
                Guild.objects.create(
                    name=guild_name,
                    description=guild_description
                )

        Player.objects.create(
            nickname=player_name,
            email=information["email"],
            bio=information["bio"],
            race=Race.objects.get(name=race_name),
            guild=Guild.objects.get(
                name=guild_name
            ) if guild_name is not None else None
        )


if __name__ == "__main__":
    main()
