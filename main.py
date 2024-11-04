import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for player_name, player_data in data.items():
        guild_data = player_data.get("guild")
        guild = None
        if guild_data:
            guild_name = guild_data.get("name")
            guild_description = guild_data.get("description")
            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description}
            )

        race_data = player_data["race"]
        race_name = race_data["name"]
        race_description = race_data.get("description", "")
        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description}
        )

        skills = race_data.get("skills", [])
        for skill_data in skills:
            skill_name = skill_data["name"]
            skill_bonus = skill_data["bonus"]
            Skill.objects.get_or_create(
                name=skill_name,
                bonus=skill_bonus,
                race=race
            )

        Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": player_data["email"],
                "bio": player_data.get("bio", ""),
                "race": race,
                "guild": guild,
            }
        )
