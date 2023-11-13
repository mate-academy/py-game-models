import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player in players:
        race, created = Race.objects.get_or_create(
            name=players[player]["race"]["name"],
            description=players[player]["race"]["description"]
        )
        if players[player]["race"]["skills"]:
            for skill in players[player]["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        Player.objects.get_or_create(
            nickname=player,
            email=players[player]["email"],
            bio=players[player]["bio"],
            race=race,
            guild=Guild.objects.get_or_create(
                name=players[player]["guild"]["name"],
                description=players[player]["guild"]["description"]
            )[0] if players[player]["guild"] else None
        )


if __name__ == "__main__":
    main()
