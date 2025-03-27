import json

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as source_file:
        players = json.load(source_file)

    for player, data in players.items():
        # player data
        nickname = player
        email = data.get("email")
        biography = data.get("bio")
        # race data
        race_name = data.get("race").get("name")
        race_description = data.get("race").get("description")
        # skill data
        skills = data.get("race").get("skills")
        # guild data
        guild_data = data.get("guild")

        race, _ = Race.objects.get_or_create(
            name=race_name,
            description=race_description
        )

        for skill in skills:
            current_skill, _ = Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                description=guild_data.get("description")
            )

        Player.objects.get_or_create(
            nickname=nickname,
            email=email,
            bio=biography,
            race=race,
            guild=guild if guild_data else None
        )


if __name__ == "__main__":
    main()
