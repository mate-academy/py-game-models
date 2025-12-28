import json
from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as f:
        players_data = json.load(f)

    for nickname, pdata in players_data.items():
        race, _ = Race.objects.get_or_create(
            name=pdata["race"]["name"],
            defaults={"description": pdata["race"].get("description", "")}
        )

        for skill_data in pdata["race"].get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                race=race,
                defaults={
                    "bonus": skill_data["bonus"]
                }
            )

        guild_data = pdata.get("guild")
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description", "")}
            )

        Player.objects.create(
            nickname=nickname,
            email=pdata["email"],
            bio=pdata.get("bio", ""),
            race=race,
            guild=guild
        )
