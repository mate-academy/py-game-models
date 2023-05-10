import init_django_orm  # noqa: F401
import json

from datetime import datetime
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        data = json.load(f)

    for nickname, player_data in data.items():
        race_data = player_data["race"]
        race, created = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )

        for skill_data in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )

        guild_data = player_data["guild"]
        if guild_data:
            guild, created = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild,
            created_at=datetime.now()
        )


if __name__ == "__main__":
    main()
