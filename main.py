import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:

    with open("players.json", "r") as json_file:
        player_dict = json.load(json_file)

    for name, properties in player_dict.items():
        race_dict = properties.get("race")
        if race_dict:
            race = Race.objects.get_or_create(
                name=race_dict.get("name"),
                description=race_dict.get("description"),
            )[0]

            skill_dicts = race_dict.get("skills", [])
            for skill_dict in skill_dicts:
                Skill.objects.get_or_create(
                    name=skill_dict.get("name"),
                    bonus=skill_dict.get("bonus"),
                    race=race,
                )

        guild_dict = properties.get("guild")

        guild = Guild.objects.get_or_create(
            name=guild_dict.get("name"),
            description=guild_dict.get("description"),
        )[0] if guild_dict else None

        Player.objects.create(
            nickname=name,
            email=properties.get("email"),
            bio=properties.get("bio"),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
