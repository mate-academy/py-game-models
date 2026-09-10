import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        report = json.load(f)

    for player_name, player_data in report.items():

        race = player_data.get("race")
        skills = race.get("skills")
        guild = player_data.get("guild")

        race_obj, _ = Race.objects.get_or_create(
            name=race.get("name"),
            description=race.get("description"),
        )

        for skill in skills:
            skill_obj, _ = Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race_obj
            )

        if guild:

            guild_obj, _ = Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
            )

        else:
            guild_obj = None

        Player.objects.create(
            nickname=player_name,
            email=player_data.get("email"),
            bio=player_data.get("bio"),
            race=race_obj,
            guild=guild_obj
        )


if __name__ == "__main__":
    main()
