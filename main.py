import json

from django.utils import timezone

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player_name, player_info in data.items():

        if not Race.objects.filter(
                name=player_info["race"]["name"]
        ).exists():
            Race.objects.create(
                name=player_info["race"]["name"],
                description=player_info["race"]["description"],
            )

        for skill in player_info["race"]["skills"]:
            if not Skill.objects.filter(
                name=skill["name"]
            ).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(
                        name=player_info["race"]["name"]
                    ),
                )

        try:
            if not Guild.objects.filter(
                name=player_info["guild"]["name"]
            ).exists():
                Guild.objects.create(
                    name=player_info["guild"]["name"],
                    description=player_info["guild"]["description"],
                )
        except TypeError as error:
            print(error)

        if player_info["guild"] is not None:
            guild = Guild.objects.get(
                name=player_info["guild"]["name"]
            )
        else:
            guild = None

        if not Player.objects.filter(
            nickname=player_name
        ).exists():
            Player.objects.create(
                nickname=player_name,
                email=player_info["email"],
                bio=player_info["bio"],
                race=Race.objects.get(
                    name=player_info["race"]["name"]
                ),
                guild=guild,
                created_at=timezone.now(),
            )


if __name__ == "__main__":
    main()
