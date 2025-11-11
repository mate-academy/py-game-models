import init_django_orm  # noqa: F401

import json

from typing import Any

from db.models import Race, Skill, Player, Guild


def get_data() -> dict[str, Any]:
    try:
        with open("players.json", "r") as p_file:
            return json.load(p_file)
    except FileNotFoundError as e:
        raise SystemExit(f"File not found: {e}")


def create_guild(name: str,
                 description: str | None) -> Guild:
    guild, _ = Guild.objects.get_or_create(
        name=name,
        defaults={"description": description}
    )
    return guild


def create_race(name: str,
                description: str | None) -> Race:
    race, _ = Race.objects.get_or_create(
        name=name,
        description=description
    )
    return race


def create_skill(name: str,
                 bonus: str,
                 race: Race) -> Skill:
    skill, _ = Skill.objects.get_or_create(
        name=name,
        race=race,
        bonus=bonus
    )
    return skill


def create_player(name: str,
                  email: str,
                  bio: str,
                  race: Race,
                  guild: Guild) -> Player:
    player, _ = Player.objects.get_or_create(
        nickname=name,
        email=email,
        bio=bio,
        race=race,
        guild=guild
    )
    return player


def main() -> None:
    data = get_data()

    for name, value in data.items():
        nickname = name
        email = value["email"]
        bio = value["bio"]
        guild = value["guild"] if value["guild"] else None
        race = value["race"]
        skills = race["skills"] if race["skills"] else None

        if guild:
            guild = create_guild(
                guild["name"],
                guild["description"]
            )

        race = create_race(
            race["name"],
            race["description"]
        )

        if skills:
            for skill in skills:
                create_skill(skill["name"], skill["bonus"], race)

        create_player(nickname, email, bio, race, guild)


if __name__ == "__main__":
    main()
