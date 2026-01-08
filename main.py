import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        user_data = json.load(f)
    for player_name, data in user_data.items():
        race_data = data.get("race", {})
        race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={
                "description": race_data.get("description", "")
            }
        )
        skills_list = race_data.get("skills", [])
        for skill in skills_list:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                defaults={
                    "bonus": skill.get("bonus"),
                    "race": race})
        guild_instance = None
        data_guild = data.get("guild")
        if data_guild:
            guild_instance, _ = Guild.objects.get_or_create(
                name=data_guild.get("name"),
                defaults={
                    "description": data_guild.get("description")
                }
            )
        Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": data.get("email"),
                "bio": data.get("bio"),
                "race": race,
                "guild": guild_instance
            }
        )


if __name__ == "__main__":
    main()
