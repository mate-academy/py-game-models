import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as data_file:
        data = json.load(data_file)
    print(data)
    for player, player_data in data.items():
        race_info = player_data.get("race")
        race_player, _ = Race.objects.get_or_create(
            name=race_info.get("name"),
            description=race_info.get("description")
        )
        skills = race_info.get("skills")
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race_player
            )

        guild_info = player_data.get("guild")
        if guild_info:
            guild_player, _ = Guild.objects.get_or_create(
                name=guild_info.get("name"),
                description=guild_info.get("description")
            )
        else:
            guild_player = None
        Player.objects.get_or_create(
            nickname=player,
            email=player_data.get("email"),
            bio=player_data.get("bio"),
            race=race_player,
            guild=guild_player

        )


if __name__ == "__main__":
    main()
