from pathlib import Path
import json
from db.models import Player, Race, Skill, Guild


def import_players(file_path: Path) -> None:
    with file_path.open(encoding="utf-8") as f:
        players_data = json.load(f)

    for player_data in players_data:
        race, _ = Race.objects.get_or_create(name=player_data["race"])
        guild_name = player_data.get("guild")
        guild = None
        if guild_name:
            guild, _ = Guild.objects.get_or_create(name=guild_name)

        player = Player.objects.create(
            nickname=player_data["nickname"],
            email=player_data["email"],
            bio=player_data.get("bio", ""),
            race=race,
            guild=guild,
        )

        for skill_name in player_data.get("skills", []):
            skill, _ = Skill.objects.get_or_create(name=skill_name)
            player.skills.add(skill)
