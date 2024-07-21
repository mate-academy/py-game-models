import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def load_from_json(path_to_file: str) -> dict:
    with open(path_to_file, "r") as file:
        data = json.load(file)
    return data


def create_race_skills(race_data: dict) -> Race:
    race, created = Race.objects.get_or_create(
        name=race_data["name"],
        defaults={"description": race_data.get("description", "")}
    )

    for skill_data in race_data.get("skills", []):
        skill, created = Skill.objects.get_or_create(
            name=skill_data["name"],
            bonus=skill_data["bonus"],
            race=race
        )
    return race


def populate_guild(guild_data: dict) -> Guild:
    if guild_data is None:
        return None
    guild, created = Guild.objects.get_or_create(
        name=guild_data["name"],
        defaults={"description": guild_data.get("description", "")}
    )
    return guild


def create_prayers(data: dict) -> None:
    for name, details in data.items():
        race = create_race_skills(details["race"])
        guild = populate_guild(details["guild"])

        player, created = Player.objects.get_or_create(
            nickname=name,
            defaults={
                "email": details["email"],
                "bio": details["bio"],
                "race": race,
                "guild": guild
            }
        )


def main() -> None:
    data = load_from_json("players.json")

    create_prayers(data)


if __name__ == "__main__":
    main()
