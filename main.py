import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players:
        players_info = json.load(players)

    for player, info in players_info.items():
        race, created = Race.objects.get_or_create(
            name=info["race"]["name"],
            description=info["race"]["description"]
        )
        for skill in info["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )
        guild = None
        if info["guild"]:
            guild, created = Guild.objects.get_or_create(
                name=info["guild"]["name"],
                description=info["guild"]["description"],
            )

        Player.objects.get_or_create(
            nickname=player,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
