import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as config_file:
        data = json.load(config_file)

    for player in data:
        email = data[player]["email"]
        bio = data[player]["bio"]

        race_name = data[player]["race"]["name"]
        race_description = data[player]["race"]["description"]
        race_skills = data[player]["race"]["skills"]

        guild_info = data[player]["guild"]

        race_id = Race.objects.get_or_create(
            name=race_name,
            description=race_description
        )[0].id

        if race_skills:
            for skill in race_skills:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race_id=race_id
                )

        guild_id = None
        if guild_info:
            guild_id = Guild.objects.get_or_create(
                name=guild_info["name"],
                description=guild_info["description"]
            )[0].id

        Player.objects.create(
            nickname=player,
            email=email,
            bio=bio,
            race_id=race_id,
            guild_id=guild_id
        )


if __name__ == "__main__":
    main()
