import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_data = json.load(file)

    for nickname, player_data in players_data.items():
        race_data = player_data.get("race")
        guild_data = player_data.get("guild")
        skill_data = race_data.get("skills")

        race_data, created = Race.objects.get_or_create(
            name=race_data.get("name"),
            description=race_data.get("description")
        )

        for skill in skill_data:
            skill = Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race_data
            )

        if guild_data:
            guild_data, created = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                description=guild_data.get("description")
            )

        Player.objects.get_or_create(
            nickname=nickname,
            email=player_data.get("email"),
            bio=player_data.get("bio"),
            race=race_data,
            guild=guild_data
        )


if __name__ == "__main__":
    main()
