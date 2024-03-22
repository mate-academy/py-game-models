import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def load_data_from_json(filename: str) -> dict:
    with open(filename, "r") as file:
        return json.load(file)


def create_races(data: dict) -> dict:
    races = {}
    for player_info in data.values():
        race_info = player_info["race"]
        race_name = race_info["name"]
        race_description = race_info["description"]
        if race_name not in races:
            races[race_name] = Race.objects.create(
                name=race_name,
                description=race_description
            )
    return races


def create_skills(data: dict, races: dict) -> None:
    existing_skills = set(Skill.objects.values_list("name", flat=True))
    for player_info in data.values():
        race_name = player_info["race"]["name"]
        race = races[race_name]
        for skill_info in player_info["race"]["skills"]:
            if skill_info["name"] not in existing_skills:
                Skill.objects.create(
                    name=skill_info["name"],
                    bonus=skill_info["bonus"],
                    race=race
                )
                existing_skills.add(skill_info["name"])


def create_guilds(data: dict) -> dict:
    guilds = {}
    for player_info in data.values():
        guild_info = player_info["guild"]
        if guild_info:
            guild_name = guild_info["name"]
            if guild_name not in guilds:
                guilds[guild_name] = Guild.objects.create(
                    name=guild_name,
                    description=guild_info.get("description", "")
                )
    return guilds


def create_players(data: dict, races: dict, guilds: dict) -> None:
    for nickname, player_info in data.items():
        race_name = player_info["race"]["name"]
        guild_name = (player_info["guild"]["name"]
                      if player_info["guild"] else None)
        Player.objects.create(
            nickname=nickname,
            email=player_info["email"],
            bio=player_info["bio"],
            race=races[race_name],
            guild=guilds.get(guild_name)
        )


def main() -> None:
    data = load_data_from_json("players.json")
    races = create_races(data)
    create_skills(data, races)
    guilds = create_guilds(data)
    create_players(data, races, guilds)


if __name__ == "__main__":
    main()
