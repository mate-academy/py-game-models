import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player_name, player_atr in players.items():
        guild = player_atr.get("guild")
        race = player_atr.get("race")
        if guild:
            guild_obj, guild_created = Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
            )
        else:
            guild_obj = None

        race_obj, race_created = Race.objects.get_or_create(
            name=race.get("name"),
            description=race.get("description")
        )
        skills = race.get("skills")
        if skills:
            for skill in skills:
                Skill.objects.get_or_create(name=skill.get("name"),
                                            bonus=skill.get("bonus"),
                                            race=race_obj)

        Player.objects.get_or_create(
            nickname=player_name,
            email=player_atr.get("email"),
            bio=player_atr.get("bio"),
            race=race_obj,
            guild=guild_obj

        )


if __name__ == "__main__":
    main()
