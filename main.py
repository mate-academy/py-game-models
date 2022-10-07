import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json", "r") as read_file:
        players = json.load(read_file)

    for player in players:
        if not Race.objects.filter(
                name=players[player]["race"]["name"]
        ).exists():
            race = Race.objects.create(
                name=players[player]["race"]["name"],
                description=players[player]["race"]["description"]
            )
        else:
            race = Race.objects.get(name=players[player]["race"]["name"])

        for skill in players[player]["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        if players[player]["guild"]:
            if not Guild.objects.filter(
                    name=players[player]["guild"]["name"]
            ).exists():
                guild = Guild.objects.create(
                    name=players[player]["guild"]["name"],
                    description=players[player]["guild"]["description"]
                )
            else:
                guild = Guild.objects.get(
                    name=players[player]["guild"]["name"]
                )
        else:
            guild = None

        Player.objects.create(
            nickname=player,
            email=players[player]["email"],
            bio=players[player]["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
