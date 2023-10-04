import os

import init_django_orm  # noqa: F401
from db.models import (
    Race, Skill, Player, Guild
)
from support_funcs import (
    load_json_data,
    model_attrs,
    create_model_item,

)


def update_race_and_skill_tables(json_data: str) -> None:
    players = load_json_data(json_data)
    for player_name, player_data in players.items():
        race = player_data["race"]
        race_name, skills = race["name"], race["skills"]
        player_race = model_attrs(Race, race)
        create_model_item(Race, player_race)

        for skill in skills:
            race_skill = model_attrs(Skill, skill)
            current_race = Race.objects.get(name=f"{race_name}")
            race_skill["race"] = current_race
            create_model_item(Skill, race_skill)


def update_guild_table(json_data: str) -> None:
    players = load_json_data(json_data)
    for player_name, player_data in players.items():
        guild_info = player_data["guild"]
        if isinstance(guild_info, dict):
            guild = model_attrs(Guild, guild_info)
            create_model_item(Guild, guild)


def update_player_table(json_data: str) -> None:
    players = load_json_data(json_data)
    for player_name, player_data in players.items():
        player = model_attrs(Player, player_data, rest_keys="created_at")
        race_name = player_data["race"]["name"]
        if not isinstance(player_data["guild"], dict):
            player.pop("guild")
        else:
            guild_name = player_data["guild"]["name"]
            player["guild"] = Guild.objects.get(name=guild_name)

        player["nickname"] = player_name
        player["race"] = Race.objects.get(name=race_name)
        create_model_item(Player, player)


def main() -> None:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    players_path = os.path.join(current_dir, "players.json")
    update_race_and_skill_tables(players_path)
    update_guild_table(players_path)
    update_player_table(players_path)


if __name__ == "__main__":
    main()
