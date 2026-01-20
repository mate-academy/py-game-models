import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json", "r") as f:
        player_data = json.load(f)

    for player_name, player_info in player_data.items():
        email = player_info["email"]
        bio = player_info["bio"]

        race_data = player_info["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )

        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"], race=race, bonus=skill_data["bonus"]
            )

        guild_data = player_info.get("guild")
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
            )

        Player.objects.create(
            nickname=player_name,
            email=email,
            bio=bio,
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
