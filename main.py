import init_django_orm  # noqa: F401
import json
from typing import Union
from db.models import Race, Skill, Player, Guild


def race_creating(race_dict: dict) -> Race:
    race_ = Race.objects.get_or_create(
        name=race_dict["name"],
        description=race_dict["description"]
    )
    return race_[0]


def guild_creating(guild_dict: dict) -> Union[Guild, None]:
    if guild_dict:
        guild_ = Guild.objects.get_or_create(
            name=guild_dict["name"],
            description=guild_dict["description"]
        )
        return guild_[0]
    return None


def skills_creating(skills_dict: dict) -> None:
    for skill in skills_dict["skills"]:
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
            skills_creating(gamer_values["race"])
            if not Player.objects.filter(nickname=gamer).exists():
                Player.objects.create(
                    nickname=gamer,
                    email=gamer_values["email"],
                    bio=gamer_values["bio"],
                    race=race_creating(gamer_values["race"]),
                    guild=guild_creating(gamer_values["guild"])
                )


if __name__ == "__main__":
    main()
