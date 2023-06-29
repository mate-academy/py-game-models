import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_data_file:
        players_data = json.load(players_data_file)

    for player_nickname, player_info in players_data.items():
        race_name = player_info["race"]["name"]
        race_description = player_info["race"]["description"]
        if not Race.objects.filter(name=race_name).exists():
            Race.objects.create(
                name=race_name,
                description=race_description
            )

        race = Race.objects.get(name=race_name)
        race_skills = player_info["race"]["skills"]
        for skill in race_skills:
            skill_name = skill["name"]
            skill_bonus = skill["bonus"]
            if not Skill.objects.filter(name=skill_name).exists():
                Skill.objects.create(
                    name=skill_name,
                    bonus=skill_bonus,
                    race=race
                )
        guild = None
        if player_info["guild"]:
            guild_name = player_info["guild"]["name"]
            guild_description = player_info["guild"]["description"]
            if not Guild.objects.filter(name=guild_name).exists():
                Guild.objects.create(
                    name=guild_name,
                    description=guild_description
                )

            guild = Guild.objects.get(name=guild_name)

        player_email = player_info["email"]
        player_bio = player_info["bio"]
        Player.objects.create(
            nickname=player_nickname,
            email=player_email,
            bio=player_bio,
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
