import json
from db.models import Race, Skill, Guild, Player

def main() -> None:
    with open("players.json", encoding="utf-8") as file:
        data = json.load(file)

    for player_name, player_data in data.items():
        race_data = player_data.get("race")
        guild_data = player_data.get("guild")
        skills_data = race_data.get("skills", []) if race_data else []

        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")},
        )

        for skill_info in skills_data:
            Skill.objects.get_or_create(
                name=skill_info["name"],
                race=race,
                defaults={"bonus": skill_info["bonus"]},
            )

        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description") or ""},
            )

        Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild,
            },
        )
