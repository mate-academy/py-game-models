import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player, player_info in players.items():
        race = player_info.get("race")
        if race:
            race, bool_ = Race.objects.get_or_create(
                name=race.get("name"),
                description=race.get("description")
            )

        guild = player_info.get("guild")
        if guild:
            guild, bool_ = Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
            )

        skills = player_info.get("race").get("skills")
        if skills:
            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=race
                )

        Player.objects.create(
            nickname=player,
            email=player_info.get("email"),
            bio=player_info.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
