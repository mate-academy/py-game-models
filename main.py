import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_data in players_data:
        race = player_data.get("race")
        description = player_data.get("description")
        if race:
            Race.objects.get_or_create(name=race,description=description)

    for player_data in players_data:
        race = player_data.get("race")
        if race:
            skills = player_data.get("skills")
            for skill in skills:
                skill_name = skill.get("name")
                skill_bonus = skill.get("bonus")
                if skill_name and skill_bonus:
                    Skill.objects.get_or_create(
                        name=skill_name,
                        bonus=skill_bonus
                    )


    for player_data in players_data:
        guild = player_data.get("guild")
        description = player_data.get("description")
        if guild:
            Guild.objects.get_or_create(name=guild, description=description)

    for player_data in players_data:
        nickname = player_data.get("nickname")
        if nickname:
            Player.objects.get_or_create(
                nickname=nickname,
                email=player_data.get("email"),
                bio=player_data.get("bio"),
                race=player_data.get("race"),
                guild=player_data.get("guild")
            )


if __name__ == "__main__":
    main()
