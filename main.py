import json
from pathlib import Path

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with Path("players.json").open(
        encoding="utf-8",
    ) as file:
        data = json.load(file)

    for nickname, player_data in data.items():
        race_data = player_data["race"]

        race, created = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={
                "description": race_data["description"],
            },
        )

        print(race.name, created)

        for skill_data in race_data["skills"]:
            skill, skill_created = Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race,
                },
            )

            print(skill.name, skill_created)

        guild_data = player_data.get("guild")
        guild = None

        if guild_data:
            guild, guild_created = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={
                    "description": guild_data.get("description"),
                },
            )

            print(guild.name, guild_created)

        player, player_created = Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild,
            },
        )

        print(player.nickname, player_created)

        print(f"Player: {nickname}")
        print(f"Race: {race_data['name']}")

        if guild_data:
            print(f"Guild: {guild_data['name']}")
        else:
            print("Guild: None")


if __name__ == "__main__":
    main()
