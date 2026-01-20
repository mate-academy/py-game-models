import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_data = json.load(file)

    for name, attribute in players_data.items():
        race_data = attribute.get("race")
        if race_data:
            race_obj, created = Race.objects.get_or_create(
                name=race_data.get("name"),
                description=race_data.get("description")
            )
        else:
            race_obj = None

        skills_date = race_data.get("skills") if race_data else []
        for skill in skills_date:
            if skill.get("name") and skill.get("bonus"):
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_obj
                )
        guild_data = attribute.get("guild")
        if guild_data:
            guild_obj, created = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                description=guild_data.get("description")
            )
        else:
            guild_obj = None

        email = attribute.get("email")
        bio = attribute.get("bio")

        Player.objects.create(
            nickname=name,
            email=email,
            bio=bio,
            race=race_obj,
            guild=guild_obj
        )


if __name__ == "__main__":
    main()
