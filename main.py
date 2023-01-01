import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json") as players_file:
        players_dict = json.load(players_file)

    for player_name, player in players_dict.items():
        race_name = player["race"]["name"]
        race_description = player["race"]["description"]
        if not Race.objects.filter(name=race_name).exists():
            race = Race.objects.create(
                name=race_name, description=race_description
            )
            for skill in player["race"]["skills"]:
                Skill.objects.create(
                    name=skill["name"], bonus=skill["bonus"], race=race
                )
        guild = None
        if player["guild"]:
            guild_name = player["guild"]["name"]
            guild_description = (
                player["guild"]["description"]
                if player["guild"]["description"]
                else None
            )
            if not Guild.objects.filter(name=guild_name).exists():
                guild = Guild.objects.create(
                    name=guild_name, description=guild_description
                )
            else:
                guild = Guild.objects.get(name=guild_name)

        if not Player.objects.filter(nickname=player_name).exists():
            Player.objects.create(
                nickname=player_name,
                email=player["email"],
                bio=player["bio"],
                race=race,
                guild=guild,
            )


if __name__ == "__main__":
    main()
