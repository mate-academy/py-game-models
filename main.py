import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def get_race(race_info: dict) -> Race:
    race, _ = Race.objects.get_or_create(
        name=race_info["name"],
        description=race_info["description"]
    )
    for skill_info in race_info["skills"]:
        _ = get_skill(skill_info, race)
    return race


def get_guild(guild_info: dict) -> Guild | None:
    if not guild_info:
        return None
    guild, _ = Guild.objects.get_or_create(
        name=guild_info["name"],
        description=guild_info["description"]
    )
    return guild


def get_skill(skill_info: dict, race: Race) -> Skill | None:
    if not skill_info:
        return None
    skill, _ = Skill.objects.get_or_create(
        name=skill_info["name"],
        bonus=skill_info["bonus"],
        race=race
    )
    return skill


def main() -> None:
    with open("players.json", "r") as data_source:
        players = json.load(data_source)
    for player_name, player_data in players.items():
        _ = Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": get_race(player_data["race"]),
                "guild": get_guild(player_data["guild"])
            }
        )


if __name__ == "__main__":
    main()
