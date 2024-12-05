import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player, players_data in players.items():
        race, _ = Race.objects.get_or_create(
            name=players_data["race"]["name"],
            description=players_data["race"]["description"],
        )

        skills = players_data["race"]["skills"]
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race,
            )

        if players_data["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=players_data["guild"]["name"],
                description=players_data["guild"]["description"],
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=player,
            email=players_data["email"],
            bio=players_data["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
