import json

import init_django_orm  # noqa: F401

from db.models import Guild, Player, Race, Skill


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, player_data in players.items():
        race_data = player_data.get("race")
        if race_data is None:
            continue

        race_name = race_data.get("name")
        if race_name is None:
            continue

        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_data.get("description", "")},
        )

        guild = None
        guild_data = player_data.get("guild")
        if guild_data is not None:
            guild_name = guild_data.get("name")
            if guild_name is not None:
                guild, _ = Guild.objects.get_or_create(
                    name=guild_name,
                    defaults={"description": guild_data.get("description")},
                )

        for skill_data in race_data.get("skills", []):
            skill_name = skill_data.get("name")
            if skill_name is None:
                continue

            Skill.objects.get_or_create(
                name=skill_name,
                defaults={
                    "bonus": skill_data.get("bonus"),
                    "race": race,
                },
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data.get("email"),
                "bio": player_data.get("bio"),
                "race": race,
                "guild": guild,
            },
        )


if __name__ == "__main__":
    main()
