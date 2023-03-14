import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_data_file:
        dict_players = json.load(players_data_file)

    for player in dict_players:
        race_data = dict_players[player]["race"]
        if Race.objects.filter(
                name=race_data["name"]
        ).exists() is False:
            race = Race.objects.create(
                name=race_data["name"],
                description=race_data["description"]
            )
        else:
            race = Race.objects.get(
                name=race_data["name"]
            )

        guild_data = dict_players[player]["guild"]
        if guild_data is not None:
            if Guild.objects.filter(
                    name=guild_data["name"]
            ).exists() is False:
                guilt = Guild.objects.create(
                    name=guild_data["name"],
                    description=guild_data["description"]
                )
            else:
                guilt = Guild.objects.get(
                    name=guild_data["name"]
                )
        else:
            guilt = None

        for skill in race_data["skills"]:
            if Skill.objects.filter(name=skill["name"]).exists() is False:
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(
                        name=race_data["name"]
                    )
                )

        Player.objects.create(
            nickname=player,
            email=dict_players[player]["email"],
            bio=dict_players[player]["bio"],
            race=race,
            guild=guilt
        )


if __name__ == "__main__":
    main()
