import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player in players:
        if players[player].get("guild"):
            Guild.objects.get_or_create(
                name=players[player]["guild"]["name"],
                description=players[player]["guild"]["description"],
            )

        race_obj = Race.objects.get_or_create(
            name=players[player]["race"]["name"],
            description=players[player]["race"]["description"],
        )

        for skills in players[player]["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skills["name"],
                bonus=skills["bonus"],
                race=race_obj[0],
            )

        guild_obj = Guild.objects.get(
            name=(players[player]["guild"]["name"])
        ) if players[player].get("guild") else None

        Player.objects.get_or_create(
            nickname=player,
            email=players[player]["email"],
            bio=players[player]["bio"],
            race=race_obj[0],
            guild=guild_obj,
        )


if __name__ == "__main__":
    main()
