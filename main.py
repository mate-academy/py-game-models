import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player_key, player_value in players.items():
        race_data = player_value.get("race")
        if race_data:
            skills_data = race_data.get("skills", [])
            race_args = (
                {
                    key: value for key, value in race_data.items()
                    if key != "skills"
                }
            )
            race_instance, created = Race.objects.get_or_create(**race_args)
            for skill in skills_data:
                skill_instance, created = (
                    Skill.objects.get_or_create(**skill, race=race_instance)
                )

        guild_data = player_value.get("guild")
        if guild_data:
            guild_instance, created = Guild.objects.get_or_create(**guild_data)
        else:
            guild_instance = None

        Player.objects.create(
            nickname=player_key,
            email=player_value["email"],
            bio=player_value["bio"],
            race=race_instance,
            guild=guild_instance
        )


if __name__ == "__main__":
    main()
