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
        race = None
        guild_data = player.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description")}
            )
        race_data = player.get("race")
        if race_data:
            race, _ = Race.objects.get_or_create(
                name=race_data.get("name"),
                defaults={"description": race_data.get("description")}
            )
            skills = race_data.get("skills")
            if skills:
                for skill in skills:
                    Skill.objects.get_or_create(
                        name=skill.get("name"),
                        defaults={"bonus": skill.get("bonus")},
                        race=race
                    )
        Player.objects.create(
            nickname=nickname,
            email=player.get("email"),
            bio=player.get("bio"),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
