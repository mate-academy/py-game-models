import init_django_orm  # noqa: F401

import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_data = json.load(file)

    for player_name in players_data:
        player_data = players_data[player_name]
        race_data = player_data["race"]
        if isinstance(race_data, dict):
            race_name = race_data.get("name")
            race_description = race_data.get("description", "")
        else:
            race_name = race_data
            race_description = ""

        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={
                "description": race_description
            }
        )

        skills_data = player_data.get("race").get("skills", [])
        for skill in skills_data:
            skill_name = skill.get("name")
            skill_bonus = skill.get("bonus")
            Skill.objects.get_or_create(
                name=skill_name, bonus=skill_bonus, race=race
            )

        guild_data = player_data.get("guild")
        guild = None
        if guild_data:
            if isinstance(guild_data, str):
                guild, _ = Guild.objects.get_or_create(name=guild_data)
            elif isinstance(guild_data, dict):
                guild_name = guild_data.get("name")
                guild_description = guild_data.get("description", None)
                guild, _ = Guild.objects.get_or_create(
                    name=guild_name,
                    defaults={
                        "description": guild_description
                    }
                )

        Player.objects.create(
            nickname=player_name,
            email=player_data.get("email", ""),
            bio=player_data.get("bio", ""),
            race=race,
            guild=guild
        )
