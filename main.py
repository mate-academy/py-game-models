import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players:

        loaded_players = json.load(players)

    for player_name, player_info in loaded_players.items():

        guild_info = player_info.get("guild")
        race_info = player_info.get("race")
        skills = race_info.get("skills")

        if guild_info:
            guild, _ = Guild.objects.get_or_create(
                name=guild_info.get("name"),
                description=guild_info.get("description")
            )
        else:
            guild = None

        race, _ = Race.objects.get_or_create(
            name=race_info.get("name"),
            description=race_info.get("description"))

        for skill in skills:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race
            )

        Player.objects.get_or_create(
            nickname=player_name,
            email=player_info.get("email"),
            bio=player_info.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
