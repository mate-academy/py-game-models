import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as json_file:
        loaded_players = json.load(json_file)

    for player, info in loaded_players.items():

        race, _ = Race.objects.get_or_create(
            name=info["race"]["name"], description=info["race"]["description"]
        )

        guild = None
        if info["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=info["guild"]["name"],
                description=info["guild"]["description"],
            )

        Player.objects.get_or_create(
            nickname=player,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild
        )

        for skill in info["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"], bonus=skill["bonus"], race=race
            )


if __name__ == "__main__":
    main()
