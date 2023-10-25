import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as data_file:
        data_source = json.load(data_file)

    for player, info in data_source.items():

        race_info = info["race"]
        skill_info = info["race"]["skills"]
        guild_info = info["guild"]

        race, _ = Race.objects.get_or_create(
            name=race_info["name"],
            description=race_info["description"],
        )

        for skill in skill_info:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race,
            )

        if guild_info:
            guild, _ = Guild.objects.get_or_create(
                name=guild_info["name"],
                description=guild_info["description"],
            )
        else:
            guild = None

        Player.objects.create(
            nickname=player,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
