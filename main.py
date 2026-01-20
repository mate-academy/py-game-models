import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)

    for player_name, player_dict in players.items():
        race, race_created = Race.objects.get_or_create(
            name=player_dict["race"]["name"],
            description=player_dict["race"]["description"]
        )

        for skills in player_dict["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skills["name"],
                bonus=skills["bonus"],
                race=race
            )

        if player_dict["guild"]:
            guild, guild_created = Guild.objects.get_or_create(
                name=player_dict["guild"]["name"],
                description=player_dict["guild"]["description"]
            )
        else:
            guild = None

        Player.objects.create(
            nickname=player_name,
            email=player_dict["email"],
            bio=player_dict["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
