import json
from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players_data = json.load(file)

    for username, player_data in players_data.items():

        race_data = player_data["race"]

        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={
                "description": race_data.get("description", "")
            }
        )

        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race
                }
            )

        guild_data = player_data.get("guild")
        guild = None

        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={
                    "description": guild_data.get("description")
                }
            )

        Player.objects.get_or_create(
            nickname=username,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild
            }
        )
