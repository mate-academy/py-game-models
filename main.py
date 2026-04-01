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
        for skill in players[player]["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        guild = players[player].get("guild")
        if guild:
            guild, created = Guild.objects.get_or_create(
                name=players[player]["guild"]["name"],
                description=players[player]["guild"]["description"]
            )

        Player.objects.create(
            nickname=player,
            email=players[player]["email"],
            bio=players[player]["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
