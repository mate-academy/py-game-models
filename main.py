import init_django_orm  # noqa: F401
import json
from typing import Union
from db.models import Race, Skill, Player, Guild


def race_creating(race: dict) -> Race:
    created_race = Race.objects.get_or_create(
        name=race["name"],
        description=race["description"]
    )
    return created_race[0]


def guild_creating(guild: dict) -> Union[Guild, None]:
    if guild:
        created_guild = Guild.objects.get_or_create(
            name=guild["name"],
            description=guild["description"]
        )
        return created_guild[0]
    return None


def skills_creating(skills: dict) -> None:
    for skill in skills["skills"]:
        if not Skill.objects.filter(name=skill["name"]).exists():
            Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race_creating(skills)
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
