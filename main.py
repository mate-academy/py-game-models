from typing import Callable, Union

import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def race_creating(race_dict: dict) -> Callable:
    if not Race.objects.filter(name=race_dict["race"]["name"]).exists():
        return Race.objects.create(
            name=race_dict["race"]["name"],
            description=race_dict["race"]["description"]
        )
    else:
        return Race.objects.get(name=race_dict["race"]["name"])


def guild_creating(guild_dict: dict) -> Union[Callable, None]:
    if guild_dict["guild"]:
        if not Guild.objects.filter(name=guild_dict["guild"]["name"]).exists():
            return Guild.objects.create(
                name=guild_dict["guild"]["name"],
                description=guild_dict["guild"]["description"]
            )
        else:
            return Guild.objects.get(name=guild_dict["guild"]["name"])
    else:
        return None


def skills_creating(skills_dict: dict) -> None:
    for skill in skills_dict["race"]["skills"]:
        if not Skill.objects.filter(name=skill["name"]).exists():
            Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race_creating(skills_dict)
            )


def main() -> None:
    with open("players.json") as f:
        gamers = json.load(f)
        for gamer, gamer_values in gamers.items():
            skills_creating(gamer_values)
            if not Player.objects.filter(nickname=gamer).exists():
                Player.objects.create(
                    nickname=gamer,
                    email=gamer_values["email"],
                    bio=gamer_values["bio"],
                    race=race_creating(gamer_values),
                    guild=guild_creating(gamer_values)
                )


if __name__ == "__main__":
    main()
