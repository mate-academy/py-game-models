import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_file:
        players = json.load(players_file)

    for username, user_data in players.items():
        race, _ = Race.objects.get_or_create(
            name=user_data["race"]["name"],
            description=user_data["race"]["description"],
        )

        guild = None

        if user_data["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=user_data["guild"]["name"],
                description=user_data["guild"]["description"],
            )

        Player.objects.get_or_create(
            nickname=username,
            email=user_data["email"],
            bio=user_data["bio"],
            race=race,
            guild=guild,
        )

        for skill in user_data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race,
            )


if __name__ == "__main__":
    main()
