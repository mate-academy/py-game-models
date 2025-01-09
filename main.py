import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player_data in data:
        # Process Race
        race_name = player_data["race"]["name"]
        race_description = player_data["race"].get("description", "")
        race, _ = Race.objects.get_or_create(name=race_name,
                                             defaults={
                                                 "description":
                                                     race_description})

        # Process Skills
        skills = player_data["race"].get("skills", [])
        for skill_data in skills:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={"bonus": skill_data["bonus"], "race": race}
            )

        # Process Guild
        guild_name = player_data.get("guild", {}).get("name")
        guild_description = player_data.get("guild", {}).get("description",
                                                             None)
        guild = None
        if guild_name:
            guild, _ = Guild.objects.get_or_create(
                name=guild_name, defaults={"description": guild_description}
            )

        # Process Player
        Player.objects.get_or_create(
            nickname=player_data["nickname"],
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild,
            },
        )
