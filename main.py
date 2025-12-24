from venv import create  # noqa: F401

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for name in data:
        player_data = data.get(name)
        race = player_data.get("race")
        if race:
            race_instance, created = Race.objects.get_or_create(
                name=race["name"],
                description=race["description"]
            )

            skills = race.get("skills")
            if skills:
                for skill in skills:
                    skill_instance, created = Skill.objects.get_or_create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race_instance
                    )
        guild = player_data.get("guild")
        player_guild = None
        if guild:
            player_guild, created = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )

        player, created = Player.objects.get_or_create(
            nickname=name,
            email=(player_data["email"] if player_data["email"] else None),
            bio=(player_data["bio"] if player_data["bio"] else None),
            race=race_instance,
            guild=(player_guild if player_guild else None)
        )


if __name__ == "__main__":
    main()
