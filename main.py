import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json", "r") as players_data_file:
        players_data = json.load(players_data_file)

    for player in players_data:
        race_json = players_data[player]["race"]
        race, created = Race.objects.get_or_create(
            name=race_json["name"],
            description=race_json["description"]
        )

        for skill in race_json["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        guild, created = (
            Guild.objects.get_or_create(
                name=players_data[player]["guild"]["name"],
                description=players_data[player]["guild"]["description"]
            ) if players_data[player]["guild"]
            else (None, False)
        )

        Player.objects.create(
            nickname=player,
            email=players_data[player]["email"],
            bio=players_data[player]["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
