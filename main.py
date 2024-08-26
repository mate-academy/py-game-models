import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def load_players(file_path: str) -> dict:
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def get_or_create_race(race: dict) -> Race:
    get_race, created = Race.objects.get_or_create(
        name=race["name"],
        description=race["description"]
    )
    return get_race if get_race else created


def get_or_create_skills(skills: list, race: Race) -> None:
    for skill in skills:
        Skill.objects.get_or_create(
            name=skill["name"],
            bonus=skill["bonus"],
            race=race
        )


def get_or_create_guild(guild: dict) -> Guild:
    get_guild, created = Guild.objects.get_or_create(
        name=guild["name"],
        description=guild["description"]
    )

    return get_guild if get_guild else created


def main() -> None:
    path_to_file = "players.json"
    data_players = load_players(path_to_file)

    for name, attribute in data_players.items():
        data_race = attribute["race"]
        get_race = get_or_create_race(data_race)

        get_or_create_skills(data_race["skills"], get_race)

        get_guild = None
        if attribute["guild"]:
            get_guild = get_or_create_guild(attribute["guild"])

        Player.objects.get_or_create(
            nickname=name,
            email=attribute["email"],
            bio=attribute["bio"],
            race=get_race,
            guild=get_guild
        )
