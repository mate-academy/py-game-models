import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_file:
        players = json.load(players_file)

    for name, player_settings in players.items():
        race_obj, race_created = Race.objects.get_or_create(
            name=player_settings["race"]["name"],
            description=player_settings["race"]["description"]
        )

        if player_settings.get("guild"):
            guild_obj, guild_created = Guild.objects.get_or_create(
                name=player_settings["guild"]["name"],
                description=player_settings["guild"]["description"]
            )
        else:
            guild_obj = None

        skills = player_settings.get("race").get("skills")
        if skills:
            if isinstance(skills, list):
                for skill in skills:
                    skill_obj, skill_created = Skill.objects.get_or_create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race_obj
                    )

        Player.objects.create(
            nickname=name,
            email=player_settings["email"],
            bio=player_settings["bio"],
            race=race_obj,
            guild=guild_obj
        )


if __name__ == "__main__":
    main()
