import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for nickname, data in players.items():
        race, race_created = Race.objects.get_or_create(
            name=data.get("race").get("name"),
            defaults={
                "description": data.get("race").get("description")
            }
        )

        for skill in data.get("race").get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                defaults={
                    "bonus": skill.get("bonus"),
                    "race": race
                }
            )

        guild_data = data.get("guild")
        if guild_data:
            guild, guild_created = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={
                    "description": guild_data.get("description")
                }
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": data.get("email"),
                "bio": data.get("bio"),
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
