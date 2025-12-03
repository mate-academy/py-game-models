import json
from pathlib import Path

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    players_file = Path(__file__).resolve().parent / "players.json"
    with open(players_file, "r", encoding="utf-8") as f:
        players_data = json.load(f)

    for nickname, pdata in players_data.items():
        # --- Race ---
        race_obj, _ = Race.objects.get_or_create(
            name=pdata["race"]["name"],
            defaults={"description": pdata["race"].get("description", "")}
        )

        # --- Skills for race ---
        for skill_data in pdata["race"].get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race_obj,
                }
            )

        # --- Guild (can be null) ---
        guild_obj = None
        if pdata.get("guild"):
            guild_obj, _ = Guild.objects.get_or_create(
                name=pdata["guild"]["name"],
                defaults={"description": pdata["guild"].get("description")}
            )

        # --- Player ---
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": pdata["email"],
                "bio": pdata.get("bio", ""),
                "race": race_obj,
                "guild": guild_obj,
            }
        )


if __name__ == "__main__":
    main()
