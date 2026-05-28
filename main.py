import json

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player_name, player_data in players.items():
        race_data = player_data.get("race", {})
        race, created = Race.objects.get_or_create(
            name=race_data.get("name"),
            description=race_data.get("description"),
        )

        skills = race_data.get("skills", [])
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race
            )

        guild_obj = None
        guild_data = player_data.get("guild")

        if guild_data:
            guild_obj, created_guild = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                description=guild_data.get("description"),
            )

        Player.objects.create(
            nickname=player_data.get("name", player_name),
            email=player_data.get("email"),
            bio=player_data.get("bio"),
            race=race,
            guild=guild_obj
        )


if __name__ == "__main__":
    main()
