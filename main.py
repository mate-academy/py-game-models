import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as json_file:
        player_data = json.load(json_file)

    for player, data in player_data.items():
        nickname = player
        email = data["email"]
        bio = data["bio"]

        race_name = data["race"]["name"]
        race_description = data["race"]["description"]
        race_info, _ = Race.objects.get_or_create(
            name=race_name, description=race_description)

        skill_data = data["race"]["skills"]
        for skill in skill_data:
            skill_name = skill["name"]
            skill_bonus = skill["bonus"]
            Skill.objects.get_or_create(
                name=skill_name, bonus=skill_bonus, race=race_info)

        guild_data = data["guild"]
        if guild_data is not None:
            guild_name = data["guild"]["name"]
            guild_description = data["guild"]["description"]
            guild_info, _ = Guild.objects.get_or_create(
                name=guild_name, description=guild_description)
        else:
            guild_info = None

        Player.objects.get_or_create(
            nickname=nickname,
            email=email,
            bio=bio,
            guild=guild_info if guild_info is not None else None,
            race=race_info,
        )


if __name__ == "__main__":
    main()
