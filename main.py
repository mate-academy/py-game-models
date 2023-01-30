import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for player_name, player_info in players.items():
        if player_info["guild"]:
            guild_name = player_info["guild"]["name"]
            guild_description = player_info["guild"]["description"]
            if Guild.objects.filter(name=guild_name).exists() is False:
                Guild.objects.create(
                    name=guild_name,
                    description=guild_description
                )
            player_guild = Guild.objects.get(name=guild_name)
        else:
            player_guild = None

        race_name = player_info["race"]["name"]
        race_description = player_info["race"]["description"]
        if Race.objects.filter(name=race_name).exists() is False:
            Race.objects.create(name=race_name, description=race_description)
            player_race = Race.objects.get(name=race_name)
            for skill in player_info["race"]["skills"]:
                skill_name = skill["name"]
                skill_bonus = skill["bonus"]
                Skill.objects.create(
                    name=skill_name,
                    bonus=skill_bonus,
                    race=player_race
                )
        player_race = Race.objects.get(name=race_name)

        Player.objects.create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=player_race,
            guild=player_guild
        )


if __name__ == "__main__":
    main()
