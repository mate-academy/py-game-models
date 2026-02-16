import init_django_orm  # noqa: F401
import json
from pathlib import Path

from db.models import Race, Skill, Guild, Player


def main() -> None:
    json_path = Path(__file__).with_name("players.json")
    data = json.loads(json_path.read_text(encoding="utf-8"))

    for nickname, info in data.items():
        race_data = info["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "") or ""},
        )

        for spices in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=spices["name"],
                defaults={"bonus": spices["bonus"], "race": race},
            )

        guild_obj = None
        guild_data = info.get("guild")
        if guild_data is not None:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description", None)},
            )

        Player.objects.update_or_create(
            nickname=nickname,
            defaults={
                "email": info["email"],
                "bio": info["bio"],
                "race": race,
                "guild": guild_obj,
            },
        )


if __name__ == "__main__":
    main()
