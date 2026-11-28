import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for player_nickname, player_data in data.items():
        race_data = player_data["race"]
        race, created = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={
                "description": race_data["description"],
            },
        )
        skills = race_data["skills"]
        for skill_data in skills:
            skill, created = Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race,
                },
            )
        guild_data = player_data.get("guild")
        if guild_data:
            guild, created = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={
                    "description": guild_data["description"],
                }
            )
        else:
            guild = None
        player, created = Player.objects.get_or_create(
            nickname=player_nickname,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
