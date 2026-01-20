import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file_players:
        players = json.load(file_players)

    for name, value in players.items():

        race_value, race_exists = Race.objects.get_or_create(
            name=value["race"]["name"],
            description=value["race"]["description"],
        )
        if race_exists is True:
            for skill in value["race"]["skills"]:
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_value,
                )

        if value["guild"] is None:
            guild_value = None
        else:
            guild_value, guild_exists = Guild.objects.get_or_create(
                name=value["guild"]["name"],
                description=value["guild"]["description"],
            )

        Player.objects.create(
            nickname=name,
            email=value["email"],
            bio=value["bio"],
            race=race_value,
            guild=guild_value,
        )


if __name__ == "__main__":
    main()
