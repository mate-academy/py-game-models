import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_data_file:
        dict_players = json.load(players_data_file)

    for player in dict_players:
        race_data = dict_players[player]["race"]
        guild_data = dict_players[player]["guild"]

        Player.objects.create(
            nickname=player,
            email=dict_players[player]["email"],
            bio=dict_players[player]["bio"],
            race=Race.objects.get_or_create(
                name=race_data["name"],
                description=race_data["description"]
            )[0],
            guild=None if guild_data is None else Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
            )[0]
        )

        for skill in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=Race.objects.get(
                    name=race_data["name"]
                )
            )


if __name__ == "__main__":
    main()
