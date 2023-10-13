import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for player_name, player_data in data.items():

        guild = player_data["guild"]
        if guild:
            player_guild_name = guild["name"]
            player_guild_description = guild.get("description", "Null")
            guild, created = Guild.objects.get_or_create(
                name=player_guild_name, description=player_guild_description
            )

        player_race_name = player_data["race"]["name"]
        player_race_description = player_data["race"]["description"]
        race, created = Race.objects.get_or_create(
            name=player_race_name, description=player_race_description
        )

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild,
        )

        for skill_data in player_data["race"]["skills"]:
            skill_name = skill_data["name"]
            skill_bonus = skill_data["bonus"]
            skill, created = Skill.objects.get_or_create(
                name=skill_name,
                bonus=skill_bonus,
                race=race
            )
