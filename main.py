import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as data_file:
        players_data = json.load(data_file)

    for player, player_info in players_data.items():
        race_info = player_info["race"]
        skill_info = race_info["skills"]
        guild_info = player_info["guild"]

        if not Race.objects.filter(name=race_info["name"]).exists():
            new_race = Race.objects.create(
                name=race_info["name"],
                description=race_info["description"]
            )

        for skill in skill_info:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=new_race
                )

        if guild_info:
            if not Guild.objects.filter(name=guild_info["name"]).exists():
                new_guild = Guild.objects.create(
                    name=guild_info["name"],
                    description=guild_info["description"]
                )

            Player.objects.create(
                nickname=player,
                email=player_info["email"],
                bio=player_info["bio"],
                race=new_race,
                guild=new_guild,
            )

        else:
            Player.objects.create(
                nickname=player,
                email=player_info["email"],
                bio=player_info["bio"],
                race=new_race,
                guild=None
            )


if __name__ == "__main__":
    main()
