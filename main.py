import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player, data in players_data.items():
        race_info = Race.objects.get_or_create(
            name=data["race"]["name"],
            description=data["race"]["description"]
        )

        skills_data = data["race"]["skills"]
        for skill in skills_data:
            skill_name = skill["name"]
            skill_bonus = skill["bonus"]
            Skill.objects.get_or_create(
                name=skill_name,
                bonus=skill_bonus,
                race=race_info[0] if race_info[0] else None
            )

        guild_data = data["guild"]
        if guild_data is not None:
            guild_info = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
            )
        else:
            guild_info = None

        Player.objects.create(
            nickname=player,
            email=data["email"],
            bio=data["bio"],
            race=race_info[0],
            guild=guild_info[0] if guild_info is not None else None
        )


if __name__ == "__main__":
    main()
