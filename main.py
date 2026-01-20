import json
from db.models import Player, Race, Skill, Guild


def main() -> None:  # Додано 2 порожні рядки та типізацію
    with open("players.json", "r", encoding="utf-8") as f:
        players_data = json.load(f)

    for nickname, player_data in players_data.items():
        race_info = player_data["race"]
        race_obj, _ = Race.objects.get_or_create(
            name=race_info["name"],
            defaults={"description": race_info.get("description", "")}
        )

        for skill_info in race_info.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_info["name"],
                defaults={
                    "bonus": skill_info["bonus"],
                    "race": race_obj
                }
            )

        guild_obj = None
        guild_info = player_data.get("guild")
        if guild_info:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_info["name"],
                defaults={"description": guild_info.get("description")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race_obj,
                "guild": guild_obj
            }
        )
