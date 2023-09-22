import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as json_file:
        players_data = json.load(json_file)

    for player, data in players_data.items():
        nickname = player
        print(nickname)
        email = data["email"]
        bio = data["bio"]
        game_race = data["race"]["name"]
        race_description = data["race"]["description"]

        race_info = Race.objects.get_or_create(
            name=game_race,
            description=race_description
        )
        guild_data = data["guild"]
        if guild_data is not None:
            guild_name = guild_data["name"]
            guild_description = guild_data["description"]
            guild_info = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_description
            )
        else:
            guild_info = None

        skills_data = data["race"]["skills"]
        for skill in skills_data:
            skill_name = skill["name"]
            skill_bonus = skill["bonus"]
            Skill.objects.get_or_create(
                name=skill_name,
                bonus=skill_bonus,
                race=race_info[0]
            )
        Player.objects.get_or_create(
            nickname=nickname,
            email=email,
            bio=bio,
            guild=guild_info[0] if guild_info is not None else None,
            race=race_info[0]

        )


if __name__ == "__main__":
    main()
