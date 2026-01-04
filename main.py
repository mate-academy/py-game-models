import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, player_data in data.items():

        # --- RACE ---
        race_info = player_data.get("race")
        race, _ = Race.objects.get_or_create(
            name=race_info.get("name"),
            defaults={"description": race_info.get("description", "")}
        )

        # --- SKILLS ---
        for skill_info in race_info.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_info.get("name"),
                defaults={
                    "bonus": skill_info.get("bonus"),
                    "race": race
                }
            )

        # --- GUILD ---
        guild_info = player_data.get("guild")
        if guild_info:
            guild, _ = Guild.objects.get_or_create(
                name=guild_info.get("name"),
                defaults={"description": guild_info.get("description")}
            )
        else:
            guild = None

        # --- PLAYER ---
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data.get("email"),
                "bio": player_data.get("bio"),
                "race": race,
                "guild": guild,
            }
        )
