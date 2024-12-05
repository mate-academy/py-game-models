import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def get_data() -> dict:
    with open("players.json", "r") as players:
        data = json.load(players)
    return data


def create_race(info: dict[str, any]) -> Race:
    return Race.objects.get_or_create(
        name=info["race"]["name"],
        description=info["race"]["description"]
    )[0]


def create_guild(info: dict[str, any]) -> Guild:
    return (
        Guild.objects.get_or_create(
            name=info["guild"]["name"],
            description=info["guild"].get("description"),
        )[0]
        if info["guild"]
        else None
    )


def create_skills(info: dict[str, any], race: Race) -> None:
    for current_skill in info["race"]["skills"]:
        if current_skill:
            Skill.objects.get_or_create(
                name=current_skill["name"],
                bonus=current_skill["bonus"],
                race=race,
            )


def create_player(
    name: str,
    race: Race,
    guild: Guild,
    info: dict[str, any]
) -> None:
    Player.objects.get_or_create(
        nickname=name,
        email=info["email"],
        bio=info["bio"],
        race=race,
        guild=guild,
    )


def main() -> None:
    for name, info in get_data().items():
        race = create_race(info)
        guild = create_guild(info)
        create_skills(info, race)
        create_player(name, race, guild, info)


if __name__ == "__main__":
    main()
