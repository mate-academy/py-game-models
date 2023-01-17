import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as data_in:
        players = json.load(data_in)
    for name, player_info in players.items():
        player_race_info = player_info["race"]
        if not Race.objects.filter(name=player_race_info["name"]).exists():
            player_race = Race.objects.create(
                name=player_race_info["name"],
                description=player_race_info["description"])
        else:
            player_race = Race.objects.get(name=player_race_info["name"])

        list_of_player_skills = player_race_info["skills"]
        for skill in list_of_player_skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=player_race
                )
        player_guild = player_info["guild"]
        if player_info["guild"] is not None:
            player_guild_info = player_info["guild"]
            if not Guild.objects.filter(
                    name=player_guild_info["name"]
            ).exists():
                player_guild = Guild.objects.create(
                    name=player_guild_info["name"],
                    description=player_guild_info["description"]
                )
            else:
                player_guild = Guild.objects.get(
                    name=player_guild_info["name"]
                )
        Player.objects.create(
            nickname=name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=player_race,
            guild=player_guild
        )


if __name__ == "__main__":
    main()
