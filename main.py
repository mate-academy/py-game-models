import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as json_file:
        data = json.load(json_file)


    for player in data:
        player_data = data[player]
        race_data = player_data.get("race")
        skills_data = race_data.get("skills")
        guild_data = player_data["guild"]

        race_name = race_data.get("name")
        race_description = race_data.get("description")
        race, race_created = (
            Race.objects.get_or_create(
                name=race_name,
                description=race_description
            )
        )

        if skills_data:
            for skill in skills_data:
                name = skill["name"]
                bonus = skill["bonus"]
                Skill.objects.get_or_create(
                    name=name,
                    bonus=bonus,
                    race=race
                )


        guild = None
        if guild_data:
            guild, guild_created = (
                Guild.objects.get_or_create(
                    name=guild_data["name"],
                    description=guild_data["description"]
                )
            )

        Player.objects.get_or_create(
            nickname=player,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()

