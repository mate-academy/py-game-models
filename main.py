import init_django_orm  # noqa: F401
import json
from typing import Dict, List, Any, Optional
from django.db import transaction
from db.models import Race, Skill, Player, Guild


def load_race(race_data: Dict[str, Any]) -> Race:
    race, _ = Race.objects.get_or_create(
        name=race_data["name"],
        defaults={"description": race_data["description"]}
    )
    return race


def load_skill(race: Race, skills_data: List[dict]) -> None:
    for skill_data in skills_data:
        Skill.objects.get_or_create(
            name=skill_data["name"],
            bonus=skill_data["bonus"],
            race=race
        )


def load_guild(guild: Optional[dict]) -> Optional[Guild]:
    if guild:
        guild, _ = Guild.objects.get_or_create(
            name=guild["name"],
            defaults={
                "description": guild.get("description")
            }
        )
        return guild
    return None


def create_player(
        player_name: str,
        player_data: Dict[str, Any],
        race: Race,
        guild: Optional[Guild],
) -> None:
    Player.objects.get_or_create(
        nickname=player_name,
        email=player_data["email"],
        bio=player_data["bio"],
        race=race,
        guild=guild,
    )


def load_player(data: Dict[str, Any]) -> None:
    with transaction.atomic():
        for player_name, player_data in data.items():
            race = load_race(player_data["race"])
            guild = load_guild(player_data.get("guild"))
            create_player(player_name, player_data, race, guild)


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)
    load_player(data)


if __name__ == "__main__":
    main()
