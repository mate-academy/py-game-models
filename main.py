import json
from pathlib import Path

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    path = Path(__file__).resolve().parent / "players.json"
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    for nickname, pdata in data.items():
        # ---- Race ----
        race_info = pdata["race"]
        race, _ = Race.objects.get_or_create(
            name=race_info["name"],
            defaults={"description": race_info.get("description", "")},
        )

        # ---- Guild (nullable) ----
        guild = None
        guild_info = pdata.get("guild")
        if guild_info:
            guild, _ = Guild.objects.get_or_create(
                name=guild_info["name"],
                defaults={"description": guild_info.get("description")},
            )

        # ---- Skills ----
        for skill in race_info.get("skills", []) or []:
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={"bonus": skill.get("bonus", ""), "race": race},
            )

        # ---- Player ----
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": pdata["email"],
                "bio": pdata["bio"],
                "race": race,
                "guild": guild,
            },
        )


if __name__ == "__main__":
    main()
