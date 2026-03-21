import django
import json
import os
from db.models import Race, Skill, Guild, Player


def main() -> None:
    django.setup()

    json_path = os.path.join(os.path.dirname(__file__), "players.json")
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"File not found: {json_path}")

    with open(json_path, "r", encoding="utf-8") as f:
        players_data = json.load(f)

    for data in players_data:
        if not isinstance(data, dict):
            continue

        # Guild
        guild_name = data.get("guild")
        guild = None
        if guild_name:
            guild, _ = Guild.objects.get_or_create(name=guild_name)

        # Race
        race_data = data.get("race")
        if not race_data:
            continue

        if isinstance(race_data, str):
            race, _ = Race.objects.get_or_create(
                name=race_data,
                defaults={"description": ""}
            )
        else:
            race_name = race_data.get("name")
            if not race_name:
                continue
            race, _ = Race.objects.get_or_create(
                name=race_name,
                defaults={"description": race_data.get("description", "")}
            )
            # Skills
            for skill_data in race_data.get("skills", []):
                skill_name = skill_data.get("name")
                if not skill_name:
                    continue
                Skill.objects.get_or_create(
                    name=skill_name,
                    race=race,
                    defaults={"bonus": skill_data.get("bonus", "")}
                )

        # Player
        nickname = data.get("nickname")
        if not nickname:
            continue
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": data.get("email", ""),
                "bio": data.get("bio", ""),
                "race": race,
                "guild": guild,
            }
        )
