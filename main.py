import json
from pathlib import Path

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    data_path = Path(__file__).resolve().parent / "players.json"
    with data_path.open(encoding="utf-8") as f:
        players_data = json.load(f)

    for nickname, player_data in players_data.items():
        race_data = player_data.get("race")
        race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={"description": race_data.get("description")},
        )

        guild_data = player_data.get("guild")
        if guild_data is not None:
            guild, _ = Guild.objects.get_or_create(
                name=(
                    guild_data.get("name")
                    if guild_data.get("name")
                    else None
                ),
                defaults={
                    "description":
                        guild_data.get("description")
                        if guild_data.get("description")
                        else None
                },
            )
        else:
            guild = None

        for skill in race_data.get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                defaults={"bonus": skill.get("bonus"), "race": race},
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data.get("email"),
                "bio": player_data.get("bio"),
                "guild": guild,
                "race": race
            },
        )


if __name__ == "__main__":
    main()
