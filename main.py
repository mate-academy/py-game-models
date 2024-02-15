import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        data = json.load(f)

    for player_name, player_info in data.items():
        race_info = player_info["race"]
        race, create_race = Race.objects.get_or_create(
            name=race_info["name"],
            description=race_info.get("description")
        )

        guild_info = player_info["guild"]
        if guild_info:
            guild, _ = Guild.objects.get_or_create(
                name=guild_info["name"],
                description=guild_info.get("description")
            )

        skills_info = race_info.get("skills")
        if create_race:
            for skill_info in skills_info:
                Skill.objects.get_or_create(
                    name=skill_info["name"],
                    bonus=skill_info["bonus"],
                    race=race
                )

        Player.objects.create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild if guild_info else None,
        )


if __name__ == "__main__":
    main()
