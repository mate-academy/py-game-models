import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json") as players_file:
        players = json.load(players_file)

    for player_name, player_info in players.items():
        race = player_info["race"]
        skills = race["skills"]
        guild = player_info["guild"]

        create_race(race)
        create_skills(skills, race)
        create_guild(guild)

        if not Player.objects.filter(nickname=player_name).exists():
            Player.objects.create(
                nickname=player_name,
                email=player_info["email"],
                bio=player_info["bio"],
                race_id=get_race_id(race),
                guild_id=get_guild_id(guild)
            )


def get_guild_id(guild: dict) -> int:
    if guild:
        return Guild.objects.get(name=guild["name"]).id


def create_guild(guild: dict) -> None:
    if guild and not Guild.objects.filter(name=guild["name"]).exists():
        Guild.objects.create(
            name=guild["name"],
            description=guild["description"]
        )


def get_race_id(race: dict) -> int:
    return Race.objects.get(name=race["name"]).id


def create_skills(skills: list, race: dict) -> None:
    for skill in skills:
        if not Skill.objects.filter(name=skill["name"]).exists():
            Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race_id=get_race_id(race)
            )


def create_race(race: dict) -> None:
    if not Race.objects.filter(name=race["name"]).exists():
        Race.objects.create(
            name=race["name"],
            description=race["description"]
        )


if __name__ == "__main__":
    main()
