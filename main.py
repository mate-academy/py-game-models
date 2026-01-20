import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        data = json.load(players_file)

    for player_name, details in data.items():
        race_data = details["race"]
        guild_data = details.get("guild")
        race, created = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )

        for skill_data in race_data.get("skills", []):
            if "name" in skill_data and "bonus" in skill_data:
                Skill.objects.get_or_create(
                    name=skill_data["name"],
                    defaults={"bonus": skill_data["bonus"], "race": race}
                )

        guild = None
        if guild_data:
            guild, created = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description", "")}
            )

        Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": details["email"],
                "bio": details["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
