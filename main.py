import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json") as data_file:
        players_data = json.load(data_file)

    for player in players_data:
        Player.objects.create(
            nickname=player,
            email=players_data[player]["email"],
            bio=players_data[player]["bio"],
            race=race(players_data[player]),
            guild=guild(players_data[player]),
        )

        for skill in players_data[player]["race"]["skills"]:
            skills(skill, players_data[player])


def race(player):
    name_of_race = player["race"]["name"]

    if not Race.objects.filter(name=name_of_race).exists():
        Race.objects.create(
            name=name_of_race,
            description=player["race"]["description"]
        )

    return Race.objects.get(name=name_of_race)


def guild(player):
    if player["guild"]:
        name_of_guild = player["guild"]["name"]

        if not Guild.objects.filter(name=name_of_guild).exists():
            Guild.objects.create(**player["guild"])

        return Guild.objects.get(name=name_of_guild)

    return None


def skills(skill, player):
    if not Skill.objects.filter(name=skill["name"]).exists():
        Skill.objects.create(**skill, race=race(player))


if __name__ == "__main__":
    main()
