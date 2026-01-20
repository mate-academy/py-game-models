import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player_name, player_info in players.items():
        email, bio, race, guild = player_info.values()
        skills = race.get("skills")

        race_obj, race_created = Race.objects.get_or_create(
            name=race.get("name"),
            description=race.get("description")
        )

        if skills:
            for skill in skills:
                Skill.objects.get_or_create(name=skill.get("name"),
                                            bonus=skill.get("bonus"),
                                            race=race_obj)

        if guild:
            guild_obj, guild_created = Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
            )
        else:
            guild_obj = None

        Player.objects.get_or_create(
            nickname=player_name,
            email=player_info.get("email"),
            bio=player_info.get("bio"),
            race=race_obj,
            guild=guild_obj

        )


if __name__ == "__main__":
    main()
