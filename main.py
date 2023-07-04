import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def create_race(race_info: dict) -> None:
    if not Race.objects.filter(
            name=race_info["name"]
    ).exists():
        Race.objects.create(
            name=race_info["name"],
            description=race_info["description"],
        )


def create_skill(skill_info: dict, race_id: int) -> None:
    if not Skill.objects.filter(
            name=skill_info["name"]
    ).exists():
        Skill.objects.create(
            name=skill_info["name"],
            bonus=skill_info["bonus"],
            race_id=race_id
        )


def create_guild(guild: dict) -> None:
    if not Guild.objects.filter(name=guild["name"]).exists():
        Guild.objects.create(
            name=guild["name"],
            description=guild["description"]
        )


def create_player(nickname: str, info: dict) -> None:
    race = info["race"]
    create_race(race)
    race_id = Race.objects.get(name=race["name"]).id
    for skill in race["skills"]:
        create_skill(skill, race_id)
    guild = info["guild"]
    if guild:
        create_guild(guild)
    Player.objects.create(
        nickname=nickname,
        email=info["email"],
        bio=info["bio"],
        race_id=race_id,
        guild_id=Guild.objects.get(
            name=guild["name"]
        ).id if guild else None
    )


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player, info in players.items():
        if not Player.objects.filter(nickname=player).exists():
            create_player(player, info)


if __name__ == "__main__":
    main()
