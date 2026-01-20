import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player in players:
        player_data = players[player]
        race = player_data["race"]
        skills = race["skills"]
        guild = player_data["guild"]

        create_race_table(race)
        create_skills_table(skills, race)
        create_guild_table(guild)

        if not Player.objects.filter(nickname=player).exists():
            Player.objects.create(
                nickname=player, email=player_data["email"],
                bio=player_data["bio"], race_id=get_race_id(race),
                guild_id=get_guild_id(guild)
            )


def create_race_table(race: dict) -> None:
    if not Race.objects.filter(name=race["name"]).exists():
        Race.objects.create(
            name=race["name"],
            description=race["description"]
        )


def get_race_id(race: dict) -> int:
    return Race.objects.get(name=race["name"]).id


def create_skills_table(skills: list[dict] | list, race: dict) -> None:
    for skill in skills:
        if not Skill.objects.filter(name=skill["name"]).exists():
            Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race_id=get_race_id(race)
            )


def create_guild_table(guild: dict | None) -> None:
    if guild and not Guild.objects.filter(name=guild["name"]).exists():
        Guild.objects.create(
            name=guild["name"], description=guild["description"]
        )


def get_guild_id(guild: dict | None) -> int | None:
    if guild:
        return Guild.objects.get(name=guild["name"]).id


if __name__ == "__main__":
    main()
