import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_file:
        data = json.load(players_file)

    for player_name, info in data.items():
        race_data = info.get("race", {})
        race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={"description": race_data.get("description")}
        )

        for skill in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                defaults={"race": race, "bonus": skill.get("bonus")}
            )

        guild_obj = None
        guild_data = info.get("guild")
        if guild_data:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description")}
            )

        Player.objects.update_or_create(
            nickname=player_name,
            defaults={
                "email": info.get("email"),
                "bio": info.get("bio"),
                "race": race,
                "guild": guild_obj
            }
        )


if __name__ == "__main__":
    main()
