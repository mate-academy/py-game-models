import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json") as file:
        players = json.load(file)

    for name, player_items in players.items():
        race = player_items["race"]

        if not Race.objects.filter(name=race["name"]).exists():
            player_race = Race.objects.create(
                name=race["name"],
                description=race["description"]
            )

            skills = race["skills"]
            for skill in skills:
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=player_race
                )

        player_guild = None
        if player_items["guild"]:
            guild = player_items["guild"]
            if not Guild.objects.filter(name=guild["name"]).exists():
                player_guild = Guild.objects.create(
                    name=guild["name"],
                    description=guild["description"]
                )
            else:
                player_guild = Guild.objects.get(name=guild["name"])

        if not Player.objects.filter(nickname=name).exists():
            Player.objects.create(
                nickname=name,
                email=player_items["email"],
                bio=player_items["bio"],
                race=Race.objects.get(name=race["name"]),
                guild=player_guild
            )


if __name__ == "__main__":
    main()
