import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players_data = json.load(players_file)

    for player_name, player_info in players_data.items():
        player_creation(player_name, player_info)


def player_creation(player_name: str, player_info: dict) -> None:
    #  GET OR CREATE RACE
    race_data = player_info["race"]
    race, created = Race.objects.get_or_create(
        name=race_data["name"],
        defaults={"description": race_data["description"]}
    )

    #  GET OR CREATE SKILL
    for skill_data in race_data["skills"]:
        Skill.objects.get_or_create(
            name=skill_data["name"],
            race=race,
            defaults={"bonus": skill_data["bonus"]}
        )

    #  GET OR CREATE GUILD
    guild_data = player_info.get("guild")
    guild = None
    if guild_data:
        guild, created = Guild.objects.get_or_create(
            name=guild_data["name"],
            defaults={"description": guild_data["description"]}
        )

    #  CREATING PLAYER
    Player.objects.get_or_create(
        nickname=player_name,
        defaults={
            "email": player_info["email"],
            "bio": player_info["bio"],
            "race": race,
            "guild": guild
        }
    )
