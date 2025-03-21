import json
import os
import django
from typing import Any, Dict
from django.conf import settings
from db.models import Race, Skill, Guild, Player

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()


def main() -> None:
    file_path: str = os.path.join(settings.BASE_DIR, "players.json")
    with open(file_path, "r") as f:
        players_data: Dict[str, Dict[str, Any]] = json.load(f)

    for nickname, data in players_data.items():
        race_data: Dict[str, Any] = data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]}
        )
        guild: Guild | None = None
        guild_data: Dict[str, Any] | None = data.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]}
            )
        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": data["email"],
                "bio": data["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
