import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)
    for player_name, information in data.items():
        race_data = information.get("race")
        skills_data = information.get("race").get("skills")
        guild = information.get("guild")

        race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            description=race_data.get("description")
        )

        for skill in skills_data:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race
            )

        guild = None
        if information.get("guild"):
            guild_info = information.get("guild")
            guild, _ = Guild.objects.get_or_create(
                name=guild_info.get("name"),
                description=guild_info.get("description")
            )

        Player.objects.get_or_create(
            nickname=player_name,
            email=information.get("email"),
            bio=information.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
