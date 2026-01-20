import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", encoding="utf-8") as f:
        players_data = json.load(f)

    for players_name, player_data in players_data.items():
        # Race
        race_data = player_data["race"]
        race_obj, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )

        # Skills
        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                race=race_obj,
                defaults={"bonus": skill_data["bonus"]}
            )

        # Guild
        guild_obj = None
        if player_data.get("guild") is not None:
            guild_data = player_data["guild"]
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )

        # Player
        Player.objects.get_or_create(
            nickname=players_name,
            defaults={
                "email": player_data["email"],
                "bio": player_data.get("bio", "") ,
                "race": race_obj,
                "guild": guild_obj,
            }
        )


if __name__ == "__main__":
    main()
