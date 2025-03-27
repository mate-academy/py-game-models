import json

import init_django_orm  # noqa: F401
from db.models import Race, Guild, Skill, Player


def create_race(add_data: dict[str, dict]) -> Race:
    race_name = add_data.get("name")
    race_description = add_data.get("description")
    race_player, _ = Race.objects.get_or_create(
        name=race_name,
        description=race_description)
    list_of_skills = add_data.get("skills")
    if list_of_skills:
        for skill in list_of_skills:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race_player)
    return race_player


def create_guild(add_data: dict[str, dict]) -> Guild:
    if add_data:
        guild_name = add_data.get("name", {})
        guild_descr = add_data.get("description", {})
        guild_player, _ = Guild.objects.get_or_create(
            name=guild_name,
            description=guild_descr)
    else:
        guild_player = None
    return guild_player


def main() -> None:
    with open("players.json", "r") as players_data:
        players = json.load(players_data)
        for player_name, add_data in players.items():
            Player.objects.get_or_create(
                nickname=player_name,
                email=add_data.get("email"),
                bio=add_data.get("bio"),
                race=create_race(add_data.get("race")),
                guild=create_guild(add_data.get("guild"))
            )


if __name__ == "__main__":
    main()
