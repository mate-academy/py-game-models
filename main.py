import init_django_orm  # noqa: F401
import json

from django.utils import timezone
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    for nickname, entry in data.items():
        race_name = entry["race"]["name"]
        race_desc = entry["race"].get("description", "")
        race, _ = Race.objects.get_or_create(name=race_name, defaults={"description": race_desc})

        for skill_data in entry["race"].get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race
                }
            )

        guild = None
        if "guild" in entry and entry["guild"] is not None:
            guild_name = entry["guild"]["name"]
            guild_desc = entry["guild"].get("description")
            guild, _ = Guild.objects.get_or_create(name=guild_name, defaults={"description": guild_desc})

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": entry["email"],
                "bio": entry["bio"],
                "race": race,
                "guild": guild,
                "created_at": timezone.now()
            }
        )


if __name__ == "__main__":
    main()
