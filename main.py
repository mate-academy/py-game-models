import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    players_data = read_data_from_file()
    for player in players_data:
        player_info = players_data[player]
        race = player_info["race"]
        guild = player_info["guild"]
        players_race = get_race(race)
        players_guild = get_guild(guild) if guild else None
        player = Player(
            nickname=player,
            email=player_info["email"],
            bio=player_info["bio"],
            race=players_race,
            guild=players_guild
        )
        player.save()


def get_race(race_data: dict) -> Race:
    race_name = race_data["name"]
    if Race.objects.filter(name=race_name).exists():
        return Race.objects.get(name=race_name)
    return create_race(race_data)


def create_race(race_info: dict) -> Race:
    race = Race(
        name=race_info["name"],
        description=race_info["description"]
    )
    race.save()
    for race_skill in race_info["skills"]:
        skill = Skill(
            name=race_skill["name"],
            bonus=race_skill["bonus"],
            race=race
        )
        skill.save()
    return race


def get_guild(guild_data: dict) -> Guild:
    guild_name = guild_data["name"]
    if Guild.objects.filter(name=guild_name).exists():
        return Guild.objects.get(name=guild_name)
    return create_guild(guild_data)


def create_guild(guild_info: dict) -> Guild:
    guild = Guild.objects.create(
        name=guild_info["name"],
        description=guild_info["description"]
    )
    return guild


def read_data_from_file() -> dict:
    with open("players.json") as file:
        return json.load(file)


if __name__ == "__main__":
    main()
