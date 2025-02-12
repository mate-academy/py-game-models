import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player, value in players.items():
        race, created = Race.objects.get_or_create(
            name=value["race"]["name"],
            description=value["race"]["description"]
        )

        guild, created = Guild.objects.get_or_create(
            name=value["guild"]["name"],
            description=value["guild"]["description"]
        ) if value["guild"] else (None, False)

        skill_list = value["race"]["skills"]
        if skill_list:
            for skill in skill_list:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race,
                )

        Player.objects.get_or_create(
            nickname=player,
            email=value["email"],
            bio=value["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
