from typing import Optional

import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def create_guild(guild_name: str, guild_script: Optional[str] = None) -> Guild:
    guild_check = Guild.objects.filter(name=guild_name).exists()
    if not guild_check:
        return Guild.objects.create(
            name=guild_name, description=guild_script
        )
    else:
        return Guild.objects.get(name=guild_name)


def create_race(
        race_name: str,
        race_script: Optional[str] = None,
        skill_package: Optional[list[dict]] = None
) -> Race:
    race_check = Race.objects.filter(name=race_name).exists()
    if race_check is False:
        race = Race.objects.create(name=race_name, description=race_script)
        if skill_package:
            for item in skill_package:
                skill_name, bonus = item["name"], item["bonus"]
                Skill.objects.create(
                    name=skill_name, bonus=bonus, race=race
                )
    else:
        race = Race.objects.get(name=race_name)
    return race


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)
    for nickname, info in data.items():
        guild = create_guild(
            info["guild"]["name"], info["guild"]["description"]
        ) if info["guild"] else None
        race = create_race(
            info["race"]["name"],
            info["race"]["description"],
            info["race"]["skills"]
        )
        Player.objects.create(
            nickname=nickname,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
