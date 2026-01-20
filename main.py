import init_django_orm  # noqa: F401
import json

from typing import Any

from db.models import Race, Skill, Player, Guild


def get_races(players: dict) -> dict[Any, Race]:
    races_obj = {}
    for player in players.values():
        if player["race"]:
            race_name = player["race"]["name"]
            if not races_obj.get(race_name):
                race_description = player["race"]["description"]
                races_obj[race_name] = Race(
                    name=race_name,
                    description=race_description
                )
    return races_obj


def get_skills(players: dict, races: dict) -> dict[Any, Skill]:
    skills_obj = {}
    for player in players.values():
        skills = player["race"]["skills"]
        for skill in skills:
            if not skills_obj.get(skill["name"]):
                race_name = player["race"]["name"]
                race_obj = races[race_name]
                skills_obj[skill["name"]] = Skill(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_obj
                )
    return skills_obj


def get_guilds(players: dict) -> dict[Any, Guild]:
    guilds_obj = {}
    for player in players.values():
        if player["guild"]:
            guild_name = player["guild"]["name"]
            if not guilds_obj.get(guild_name):
                guild_description = player["guild"]["description"]
                guilds_obj[guild_name] = Guild(
                    name=guild_name,
                    description=guild_description
                )
    return guilds_obj


def save_players(players: dict, races: dict, guilds: dict) -> None:
    for nickname, player_dict in players.items():
        race_name = (
            player_dict["race"].get("name") if player_dict["race"] else None
        )
        race_obj = races[race_name] if player_dict["race"] else None
        guild_name = (
            player_dict["guild"].get("name") if player_dict["guild"] else None
        )
        guild_obj = guilds[guild_name] if player_dict["guild"] else None
        obj, created = Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_dict["email"],
                "bio": player_dict["bio"],
                "race": race_obj,
                "guild": guild_obj
            }
        )


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
    races = get_races(players)
    skills = get_skills(players, races)
    guilds = get_guilds(players)
    for race in races.values():
        race.save()
    for skill in skills.values():
        skill.save()
    for guild in guilds.values():
        guild.save()
    save_players(players, races, guilds)


if __name__ == "__main__":
    main()
