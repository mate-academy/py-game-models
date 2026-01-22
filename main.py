import init_django_orm  # noqa: F401
from django.utils import timezone

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)
    for player_name, player_data in players_data.items():
        race_data = player_data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data.get("description", "")
        )

        skills_data = race_data.get("skills", [])
        for skill_data in skills_data:
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )

        guild_data = player_data["guild"]
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data.get("description", "")
            )
        try:
            player = Player.objects.get(nickname=player_name)
        except Player.DoesNotExist:
            player = Player(
                nickname=player_name,
                email=player_data["email"],
                bio=player_data["bio"],
                race=race,
                guild=guild,
                created_at=timezone.now()
            )
            player.save()


if __name__ == "__main__":
    main()
