import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for player_name, player_data in players.items():
        race_info = player_data["race"]["description"] or ""
        race_obj, _ = Race.objects.get_or_create(
            name = player_data["race"]["name"],
            description = race_info,
        )

        for skill in player_data["race"]["skills"]:
            Skill.objects.get_or_create(
                name = skill["name"],
                race = race_obj,
                bonus = skill["bonus"],
            )

        guild_obj = None
        if player_data["guilds"]:
            guild_name = player_data["guilds"]["name"]
            guild_description = player_data["guilds"]["description"]
            guild_obj, _ = Guild.objects.get_or_create(
                name = guild_name,
                description = guild_description,
            )

        Player.objects.update_or_create(
            nickname = player_name,
            defaults = {
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race_obj,
                "guild": guild_obj
            }
        )


if __name__ == "__main__":
    main()
