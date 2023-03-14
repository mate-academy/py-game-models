import init_django_orm  # noqa: F401

import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as player_json:
        player_data = json.load(player_json)

    for player_nickname, player_info in player_data.items():

        race = player_info.get("race")
        new_race, created = Race.objects.get_or_create(
            name=race.get("name"),
            description=race.get("description")
        )

        skills = race.get("skills")
        for skill in skills:
            Skill.objects.get_or_create(
                race=new_race,
                name=skill.get("name"),
                bonus=skill.get("bonus")
            )

        guild = player_info.get("guild")
        if guild is not None:
            new_guild, created = Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
            )
        else:
            new_guild = None

        Player.objects.get_or_create(
            nickname=player_nickname,
            email=player_info.get("email"),
            bio=player_info.get("bio"),
            race=new_race,
            guild=new_guild
        )


if __name__ == "__main__":
    main()
