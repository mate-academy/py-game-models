import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def open_json() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)
    return players


def get_or_create_race(race_name: str, race_description: str) -> None:
    race, created = Race.objects.get_or_create(
        name=race_name,
        defaults={'description': race_description}
    )
    return race


def create_races_and_skills(players_info: dict) -> None:
    races = {}

    for player in players_info:
        race_info = players_info[player]["race"]
        race_name = race_info["name"]
        race_description = race_info["description"]

        if race_name not in races:
            races[race_name] = get_or_create_race(race_name, race_description)

        race = races[race_name]
        for skill in race_info["Skill"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )


def get_or_create_guild(guild_name: str, guild_description: str) -> None:
    guild = Guild.objects.filter(name=guild_name).first()
    if guild is None:
        guild = Guild.objects.create(name=guild_name, description=guild_description)
    return guild


def create_guilds(players_info: dict) -> None:
    guilds = {}

    for player in players_info:
        guild_info = players_info[player].get("guild", {})
        guild_name = guild_info.get("name")
        guild_description = guild_info.get("description", "")

        if guild_name:
            if guild_name not in guilds:
                guilds[guild_name] = get_or_create_guild(guild_name, guild_description)


def create_players(players_info: dict) -> None:
    for players_name, players_info in players_info.items():
        race_info = players_info["race"]
        race_name = race_info["name"]
        race_description = race_info["description"]

        race = get_or_create_race(race_name, race_description)

        guild_info = players_info["guild"]
        guild_name = guild_info.get("name")
        guild_description = guild_info.get("description", "")

        guild = get_or_create_guild(guild_name, guild_description)

        Player.objects.get_or_create(
            nickname=players_name,
            defaults={
                "email": players_info["email"],
                "bio": players_info["bio"],
                "race": players_info["race"],
                "guild": players_info["guild"],
            }
        )


def main() -> None:
    players_info = open_json()
    create_races_and_skills(players_info)
    create_guilds(players_info)
    create_players(players_info)


if __name__ == "__main__":
    main()
