import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_name, player_data in players_data.items():
        race_name = player_data["race"]["name"]
        race_descript = player_data["race"].get("description", "")

        race, created = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_descript}
        )

        for skill_data in player_data["race"].get("skills", []):
            skill_name = skill_data["name"]
            skill_bonus = skill_data["bonus"]

            Skill.objects.get_or_create(
                name=skill_name,
                defaults={
                    "bonus": skill_bonus,
                    "race": race
                }
            )

        guild_data = player_data.get("guild")
        guild = None
        if guild_data:
            guild_name = guild_data["name"]
            guild_descript = guild_data.get("description")

            if guild_descript is None:
                guild_descript = ""

            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_descript}
            )

        Player.objects.get_or_create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
