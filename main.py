import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


PLAYER_FILE_NAME = "players.json"


def main() -> None:
    with open(PLAYER_FILE_NAME, "r") as file:
        player = json.load(file)

    for name, player_info in player.items():
        race = player_info.get("race")
        guild = player_info.get("guild")
        skills = race.get("skills")

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

        Player.objects.create(
            nickname=name,
            email=player_info.get("email"),
            bio=player_info.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
