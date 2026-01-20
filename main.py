import json
from typing import Any

from db.models import Player, Race, Skill, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        data: dict[str, Any] = json.load(file)

    for nickname, info in data.items():
        race_data = info["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")},
        )

        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race,
                },
            )

        guild: Guild | None = None
        guild_info = info.get("guild")
        if isinstance(guild_info, dict):
            guild, _ = Guild.objects.get_or_create(
                name=guild_info["name"],
                defaults={"description": guild_info.get("description")},
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": info["email"],
                "bio": info["bio"],
                "race": race,
                "guild": guild,
            },
        )

if __name__ == "__main__":
    main()
