import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player_name, player_info in data.items():
        race_description = player_info.get("race", {}).get("description", "")
        skills = player_info.get("race", {}).get("skills", {})

        race_obj, created = Race.objects.get_or_create(
            name=player_info.get("race", {}).get("name"),
            description=race_description
        )

        for skill in skills:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race_obj
            )

        guild = player_info.get("guild")
        guild_obj, _ = (
            Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
            )
            if guild else (None, False)
        )

        Player.objects.get_or_create(
            nickname=player_name,
            email=player_info.get("email"),
            bio=player_info.get("bio"),
            race=race_obj,
            guild=guild_obj
        )


if __name__ == "__main__":
    main()
