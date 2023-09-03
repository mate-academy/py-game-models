import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json", "r") as players_data_file:
        players_data = json.load(players_data_file)

    race_dict = {}
    guild_dict = {}

    for player in players_data:
        race_json = players_data[player]["race"]
        if race_json["name"] in race_dict:
            race = race_dict[race_json["name"]]
        else:
            race = Race.objects.create(
                name=race_json["name"],
                description=race_json["description"]
            )
            race_dict[race_json["name"]] = race

            for skill in race_json["skills"]:
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(name=race_json["name"])
                )

        if players_data[player]["guild"]:
            if players_data[player]["guild"]["name"] in guild_dict:
                guild = guild_dict[players_data[player]["guild"]["name"]]
            else:
                guild = Guild.objects.create(
                    name=players_data[player]["guild"]["name"],
                    description=players_data[player]["guild"]["description"]
                )
                guild_dict[players_data[player]["guild"]["name"]] = guild
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
