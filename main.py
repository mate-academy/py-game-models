import init_django_orm  # noqa: F401
import json
from pathlib import Path
from db.models import Race, Skill, Guild, Player

def main():
    file_path = Path("players.json")
    if not file_path.exists():
        raise FileNotFoundError("Файл players.json не знайдено!")

    with open(file_path, "r") as file:
        players_data = json.load(file)

    for nickname, player_data in players_data.items():
        # Race
        race_data = player_data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )

        skills_data = race_data.get("skills", [])
        for skill_data in skills_data:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={"bonus": skill_data["bonus"], "race": race}
            )

        guild_data = player_data.get("guild")
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description", None)}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild
            }
        )