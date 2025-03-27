import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def create_race(race_info: dict) -> int:
    race, created = Race.objects.get_or_create(
        name=race_info["name"],
        description=race_info["description"],
    )

    return race.id


def create_skill(skill_info: dict, race_id: int) -> None:
    Skill.objects.get_or_create(
        name=skill_info["name"], bonus=skill_info["bonus"], race_id=race_id
    )


def create_guild(guild: [dict, None]) -> None:
    if not guild:
        return None

    Guild.objects.get_or_create(
        name=guild["name"], description=guild["description"]
    )
    return Guild.objects.get(name=guild["name"]).id


def create_player(nickname: str, info: dict) -> None:
    race = info["race"]
    race_id = create_race(race)
    for skill in race["skills"]:
        create_skill(skill, race_id)
    guild = info["guild"]
    player_obj, created = Player.objects.get_or_create(
        nickname=nickname,
        defaults={
            "email": info["email"],
            "bio": info["bio"],
            "race_id": race_id,
            "guild_id": create_guild(guild),
        },
    )


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player, info in players.items():
        create_player(player, info)


if __name__ == "__main__":
    main()
