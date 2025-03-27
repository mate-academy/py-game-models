import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json", "r") as json_file:
        players = json.load(json_file)
    for player in players:
        race, _ = Race.objects.get_or_create(
            name=players[player]["race"]["name"],
            description=players[player]["race"]["description"]
        )
        guild = None
        if players[player].get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=players[player]["guild"]["name"],
                description=players[player]["guild"]["description"]
            )

        for skil in players[player]["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skil["name"],
                bonus=skil["bonus"],
                race=race
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
