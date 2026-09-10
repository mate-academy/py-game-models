import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        report = json.load(f)

    for player_name, player_data in report.items():

        race = player_data["race"]
        skills = race["skills"]
        guild = player_data["guild"]

        race_obj, _ = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"],
        )

        for skill in skills:
            skill_obj, _ = Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race_obj
            )

        if guild:

            guild_obj, _ = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )

        else:
            guild_obj = None

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race_obj,
            guild=guild_obj
        )


if __name__ == "__main__":
    main()
