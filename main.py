import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def race(value):
    race_name = value["race"]["name"]
    race_description = value["race"]["description"]
    if not Race.objects.filter(name=race_name).exists():
        Race.objects.create(
            name=race_name,
            description=race_description
        )


def skills_(skill, race_name):
    if not Skill.objects.filter(name=skill["name"]).exists():
        Skill.objects.create(
            name=skill["name"],
            bonus=skill["bonus"],
            race=Race.objects.get(name=race_name)
        )


def guild(value):
    if value["guild"]:
        guild_name = value["guild"]["name"]
        guild_description = value["guild"]["description"]
        if not Guild.objects.filter(name=guild_name).exists():
            Guild.objects.create(
                name=guild_name,
                description=guild_description
            )


def player_in_guild(player, value, race_name, guild_name):
    Player.objects.create(
        nickname=player,
        email=value["email"],
        bio=value["bio"],
        race=Race.objects.get(name=race_name),
        guild=Guild.objects.get(name=guild_name)
    )


def player_without_a_guild(player, value, race_name):
    Player.objects.create(
        nickname=player,
        email=value["email"],
        bio=value["bio"],
        race=Race.objects.get(name=race_name)
    )


def main():
    with open("players.json", "r") as file:
        players = json.load(file)

    for player, value in players.items():
        race_name = value["race"]["name"]
        race(value)

        skills = value["race"]["skills"]
        for skill in skills:
            skills_(skill, race_name)

        if value["guild"]:
            guild(value)
            guild_name = value["guild"]["name"]
            player_in_guild(player, value, race_name, guild_name)
        else:
            player_without_a_guild(player, value, race_name)


if __name__ == "__main__":
    main()
