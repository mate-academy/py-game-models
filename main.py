import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        players = json.load(f)

    for player_name, player_info in players.items():
        race = player_info.get("race")
        skills = race.get("skills")
        guild = player_info.get("guild")

        if race:
            race, _ = Race.objects.get_or_create(
                name=race.get("name"),
                description=race.get("description")
            )
        if skills:
            for skill in skills:
                skill, _ = Skill.objects.get_or_create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=race
                )

        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
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
