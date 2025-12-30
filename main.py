import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def load_data_from_file() -> dict:
    with open("players.json") as file:
        return json.load(file)


def create_race(race: dict) -> Race:
    created_race, created = Race.objects.get_or_create(
        name=race["name"],
        description=race["description"]
    )
    return created_race


def create_skills(skills: dict, race: Race) -> None:
    for skill in skills:
        Skill.objects.get_or_create(
            name=skill["name"],
            bonus=skill["bonus"],
            race=race
        )


def create_guild(guild: dict) -> Guild | None:
    if guild is not None:
        guild, created = Guild.objects.get_or_create(
            name=guild["name"],
            description=guild["description"]
        )
        return guild

    return None


def main() -> None:
    players = load_data_from_file()
    for name, info in players.items():
        race = create_race(info["race"])

        create_skills(info["race"]["skills"], race)

        guild = create_guild(info["guild"])

        Player.objects.get_or_create(
            nickname=name,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
