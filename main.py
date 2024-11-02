import json
from pydoc import describe

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)
    for nickname, players_info in data.items():
        race_obj, created = Race.objects.get_or_create(
            name=players_info["race"]["name"],
            defaults={
                "description": players_info["race"]["description"]
            }
        )
        skills = players_info["race"]["skills"]
        for skill in skills:
            skill_obj, created = Skill.objects.get_or_create(
                name=skill["name"],
                defaults={
                    "bonus": skill["bonus"],
                    "race": race_obj
                }
            )
        guild = data.get("guild")
        if guild:
            guild_obj, created = Guild.objects.get_or_create(
                name=guild["name"],
                defaults={
                    "description": guild["description"]
                }
            )
        else:
            guild_obj = None
        player_obj, created = Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": players_info["email"],
                "bio": players_info["bio"],
                "race": race_obj,
                "guild": guild_obj
            }
        )

if __name__ == "__main__":
    main()
