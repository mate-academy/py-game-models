import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main():
    with open("players.json", "r") as players:
        players_data = json.load(players)

    for player in players_data:
        if not Race.objects.filter(
                name=players_data[player]["race"]["name"]
        ).exists():
            race = Race.objects.create(
                name=players_data[player]["race"]["name"],
                description=players_data[player]["race"]["description"]
            )

        race = Race.objects.get(name=players_data[player]["race"]["name"])

        for skill in players_data[player]["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        if players_data[player]["guild"] is not None:
            if not Guild.objects.filter(
                    name=players_data[player]["guild"]["name"]
            ).exists():
                guild = Guild.objects.create(
                    name=players_data[player]["guild"]["name"],
                    description=players_data[player]["guild"]["description"]
                )

            guild = Guild.objects.get(
                name=players_data[player]["guild"]["name"]
            )
        else:
            guild = None

        Player.objects.create(
            nickname=player,
            email=players_data[player]["email"],
            bio=players_data[player]["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
