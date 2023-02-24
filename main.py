import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file_players:
        players = json.load(file_players)

    for name, value in players.items():

        if Race.objects.filter(name=value["race"]["name"]).exists() is False:
            race_value = Race.objects.create(
                name=value["race"]["name"],
                description=value["race"]["description"],
            )
            for skill in value["race"]["skills"]:
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_value
                )
        else:
            race_value = Race.objects.get(name=value["race"]["name"])

        if value["guild"] is None:
            guild_value = None
        else:
            if Guild.objects.filter(
                    name=value["guild"]["name"]
            ).exists() is False:

                guild_value = Guild.objects.create(
                    name=value["guild"]["name"],
                    description=value["guild"]["description"],
                )
            else:
                guild_value = Guild.objects.get(name=value["guild"]["name"])

        Player.objects.create(
            nickname=name,
            email=value["email"],
            bio=value["bio"],
            race=race_value,
            guild=guild_value,
        )


if __name__ == "__main__":
    main()
