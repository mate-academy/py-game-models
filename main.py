import json
import init_django_orm # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)

    for player_data in players.list:
        race_data = player_data.get("race")
        if not race_data:
            continue

        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )
        for skill_data in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"], bonus=skill_data["bonus"],
                race=race
            )

        guild = None
        guild_data = player_data.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description", "")}
            )

        player, created = Player.objects.get_or_create(
            nickname=player_data["nickname"],
            defaults={
                "email": player_data.get("email", ""),
                "bio": player_data.get("bio", ""),
                "race": race,
                "guild": guild,
            }
        )

        skills_data = player_data.get("skills", [])
        for skill_data in skills_data:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data.get("bonus", ""),
                    "race": race
                }
            )
