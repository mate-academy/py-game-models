import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player_name, player_data in data.items():
        race_name = player_data["race"]["name"]
        race_description = player_data["race"]["description"]
        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description}
        )

        for skill_data in player_data["race"].get("skills", []):
            Skill.objects.get_or_create(name=skill_data["name"],
                                        bonus=skill_data["bonus"], race=race)

        guild = None
        if player_data.get("guild"):
            guild_name = player_data["guild"]["name"]
            guild_description = player_data["guild"].get("description")
            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description}
            )

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
