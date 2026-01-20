import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as source:
        players_info = json.load(source)

    for player, data in players_info.items():

        current_guild = None

        if Race.objects.filter(name=data["race"]["name"]).exists():
            current_race = Race.objects.get(name=data["race"]["name"])
        else:
            current_race = Race.objects.create(
                name=data["race"]["name"],
                description=data["race"]["description"]
            )

        if data["guild"]:
            if Guild.objects.filter(name=data["guild"]["name"]).exists():
                current_guild = Guild.objects.get(name=data["guild"]["name"])
            else:
                current_guild = Guild.objects.create(
                    name=data["guild"]["name"],
                    description=data["guild"]["description"]
                )

        for skill in data["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=current_race
                )

        Player.objects.create(
            nickname=player,
            email=data["email"],
            bio=data["bio"],
            race=current_race,
            guild=current_guild
        )


if __name__ == "__main__":
    main()
