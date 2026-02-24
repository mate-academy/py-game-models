import datetime
from pathlib import Path

import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


BASE_DIR = Path(__file__).resolve().parent


def main() -> None:
    with open(BASE_DIR / "players.json", "r") as f:
        players = json.load(f)
    for nickname, player in players.items():
        guild = None
        if player.get("guild") is not None:
            guild_name = player["guild"]["name"]
            guild_description = player["guild"]["description"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description}
            )
        race_name = player["race"]["name"]
        race_description = player["race"]["description"]
        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description}
        )
        for skill in player["race"]["skills"]:
            skill_name = skill["name"]
            skill_bonus = skill["bonus"]
            Skill.objects.get_or_create(
                name=skill_name,
                defaults={"bonus": skill_bonus},
                race=race
            )
        Player.objects.create(
            nickname=nickname,
            email=player["email"],
            bio=player["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
