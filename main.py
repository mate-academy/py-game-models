import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for player_name, player_data in data.items():
        race_data = player_data.get("race", {})
        race, created = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data.get("description", "")
        )

        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data.get("bonus", ""),
                race=race
            )

        guild_data = player_data.get("guild")
        if guild_data:
            guild, created = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data.get("description", None)
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
