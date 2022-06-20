import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def main():
    with open(BASE_DIR / "players.json", "r") as file:
        players_data = json.load(file)
    for name, data in players_data.items():
        race = create_race(data["race"])
        create_skill(data["race"]["skills"], race)
        guild = create_guild(data["guild"])
        Player.objects.create(
            nickname=name,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild
        )


def create_race(race_info: dict):
    if Race.objects.filter(name=race_info["name"]).exists() is False:
        race = Race.objects.create(
            name=race_info["name"],
            description=race_info["description"]
        )
    else:
        race = Race.objects.get(name=race_info["name"])
    return race


def create_skill(skills: list, race: Race):
    for skill in skills:
        if Skill.objects.filter(name=skill["name"]).exists() is False:
            Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )


def create_guild(guild: dict):
    if guild is None:
        return None
    if Guild.objects.filter(name=guild["name"]).exists() is False:
        guild = Guild.objects.create(
            name=guild["name"],
            description=guild["description"]
        )
    else:
        guild = Guild.objects.get(name=guild["name"])
    return guild


if __name__ == "__main__":
    main()
