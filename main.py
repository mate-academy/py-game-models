import json
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from db.models import Guild, Player, Race, Skill  # noqa: E402


def main() -> None:
    with open("players.json", "r") as f:
        data = json.load(f)
    for nickname, player_data in data.items():
        race_data = player_data["race"]
        race, created = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]},
        )

        for skill_data in race_data["skills"]:
            skill, created = Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={"bonus": skill_data["bonus"], "race": race},
            )

        guild = None
        guild_data = player_data["guild"]
        if guild_data:
            guild, created = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]},
            )
        player, created = Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild,
            },
        )


if __name__ == "__main__":
    main()
