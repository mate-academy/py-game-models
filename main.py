import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for nickname, player_data in data.items():
        email = player_data["email"]
        bio = player_data["bio"]

        race_name = player_data["race"]["name"]
        race_description = (
            player_data["race"].get("description", "")
        )

        race_instance, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={
                "description": race_description
            },
        )

        skills = player_data["race"].get("skills", [])
        for skill_data in skills:
            skill_name = skill_data["name"]
            skill_bonus = skill_data["bonus"]

            skill_instance, _ = Skill.objects.get_or_create(
                name=skill_name,
                race=race_instance,
                defaults={
                    "bonus": skill_bonus,
                },
            )

        guild_data = player_data.get("guild")
        guild_instance = None
        if guild_data:
            guild_instance, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={
                    "description": guild_data.get("description")
                },
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": email,
                "bio": bio,
                "race": race_instance,
                "guild": guild_instance,
            },
        )


if __name__ == "__main__":
    main()
