import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for nickname, player_data in data.items():
        race_data = player_data["race"]

        race_object, created = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={
                "description": race_data["description"],
            }
        )

        guild_data = player_data.get("guild")
        guild_object = None

        if guild_data:
            guild_object, created = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={
                    "description": guild_data["description"],
                }
            )

        for skill_item in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_item["name"],
                defaults={
                    "bonus": skill_item["bonus"],
                    "race": race_object,
                }
            )

        Player.objects.create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],

            race=race_object,
            guild=guild_object
        )


if __name__ == "__main__":
    main()
