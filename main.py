import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def get_race(race_info: dict) -> Race:
    result = Race.objects.get_or_create(
        name=race_info["name"],
        description=race_info["description"]
    )[0]
    for skill_info in race_info["skills"]:
        _ = get_skill(skill_info, result)
    return result


def get_guild(guild_info: dict) -> Guild:
    if not guild_info:
        return None
    result = Guild.objects.get_or_create(
        name=guild_info["name"],
        description=guild_info["description"]
    )[0]
    return result


def get_skill(skill_info: dict, race: Race) -> Skill:
    if not skill_info:
        return None
    result = Skill.objects.get_or_create(
        name=skill_info["name"],
        bonus=skill_info["bonus"],
        race=race
    )[0]
    return result


def main() -> None:
    with open("players.json", "r") as data_source:
        players = json.load(data_source)
    for player_name, player_data in players.items():
        if Player.objects.filter(nickname=player_name).exists():
            continue
        race = get_race(player_data["race"])
        guild = get_guild(player_data["guild"])
        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
