import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for player, fields in data.items():
        race_data = fields["race"]

        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={
                "description": race_data.get("description", "")
            }
        )

        guild_data = fields.get("guild")

        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={
                    "description": guild_data.get("description")
                }
            )
        else:
            guild = None

        Player.objects.create(
            nickname=player,
            email=fields["email"],
            bio=fields["bio"],
            race=race,
            guild=guild
        )

        for skill_item in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_item["name"],
                defaults={
                    "bonus": skill_item["bonus"],
                    "race": race
                }
            )


if __name__ == "__main__":
    main()
