import json
from pathlib import Path
from db.models import Race, Skill, Guild, Player


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    file_path = base_dir / "db" / "tests" / "players.json"
    print(f"Reading: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for nickname, details in data.items():
        email = details.get("email")
        bio = details.get("bio")
        race_data = details.get("race")
        guild_data = details.get("guild")

        # Handle Race
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")},
        )

        # Handle Skills
        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race,
                }
            )

        # Handle Guild (can be null)
        guild = None
        if guild_data is not None:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]},
            )

        # Handle Player
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": email,
                "bio": bio,
                "race": race,
                "guild": guild,
            }
        )
