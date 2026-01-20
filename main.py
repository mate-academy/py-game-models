import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player, info in players_data.items():
        email, bio, race, guild = info.values()

        race_obj, _ = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )

        if race["skills"]:
            for skill in race["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_obj
                )

        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )

        Player.objects.get_or_create(
            nickname=player,
            email=email,
            bio=bio,
            race=race_obj,
            guild=guild,
        )


if __name__ == "__main__":
    main()
