import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for nickname, player_data in players.items():
        race_obj, created_race = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            description=player_data["race"]["description"]
        )

        for skill_data in player_data["race"].get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race_obj
            )

        guild_data = player_data.get("guild")
        guild_obj = None
        if guild_data:
            guild_obj, created_guild = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
            )

        Player.objects.get_or_create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race_obj,
            guild=guild_obj
        )


if __name__ == "__main__":
    main()
