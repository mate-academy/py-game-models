import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def crate_race(race_data: dict) -> Race:
    race, _ = Race.objects.get_or_create(
        name=race_data.get("name"),
        description=race_data.get("description")
    )
    return race


def create_skill(skills_data: dict, race: Race) -> None:
    Skill.objects.get_or_create(
        name=skills_data.get("name"),
        bonus=skills_data.get("bonus"),
        race=race
    )


def crete_guild(guild_data: dict) -> Guild | None:
    guild, _ = Guild.objects.get_or_create(
        name=guild_data.get("name"),
        description=guild_data.get("description"),
    )
    return guild


def main() -> None:
    with open("players.json") as data:
        DATA = json.load(data)

    for user_name, user_data in DATA.items():
        race = crate_race(race_data=user_data.get("race"))

        for skill in user_data.get("race").get("skills"):
            create_skill(skills_data=skill, race=race)

        guild = None
        if user_data.get("guild"):
            guild = crete_guild(user_data.get("guild"))

        Player(
            nickname=user_name,
            email=user_data.get("email"),
            bio=user_data.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
