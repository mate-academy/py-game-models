import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def open_json() -> dict:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)
    return players


def get_or_create_race(race_name: str, race_description: str) -> Race:
    race, created = Race.objects.get_or_create(
        name=race_name,
        defaults={"description": race_description}
    )
    return race


def create_races_and_skills(players_info: dict) -> None:
    races = {}

    for player, info in players_info.items():
        race_info = info["race"]
        race_name = race_info["name"]
        race_description = race_info["description"]

        if race_name not in races:
            race = get_or_create_race(race_name, race_description)
            races[race_name] = race
        else:
            race = races[race_name]

        for skill in race_info.get("skills", []):
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )


def get_or_create_guild(guild_name: str, guild_description: str) -> Guild:
    guild, created = Guild.objects.get_or_create(
        name=guild_name,
        defaults={"description": guild_description}
    )
    return guild


def create_guilds(players_info: dict) -> None:
    guilds = {}

    for player, info in players_info.items():
        guild_info = info.get("guild")

        if guild_info:
            guild_name = guild_info.get("name")
            guild_description = guild_info.get("description", "")

            if guild_name and guild_name not in guilds:
                guilds[guild_name] = get_or_create_guild(
                    guild_name, guild_description
                )


def create_players(players_info: dict) -> None:
    for player_name, player_info in players_info.items():
        race_info = player_info["race"]
        race_name = race_info["name"]
        race_description = race_info["description"]

        race = get_or_create_race(race_name, race_description)

        guild_info = player_info.get("guild")
        guild = None

        if guild_info:
            guild_name = guild_info.get("name")
            guild_description = guild_info.get("description", "")
            guild = get_or_create_guild(
                guild_name, guild_description
            ) if guild_name else None

        Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": player_info["email"],
                "bio": player_info.get("bio", ""),
                "race": race,
                "guild": guild,
            }
        )



def main() -> None:
    players_info = open_json()
    create_races_and_skills(players_info)
    create_guilds(players_info)
    create_players(players_info)


if __name__ == "__main__":
    main()
