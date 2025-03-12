import json

from django.utils import timezone

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player_name, player_info in data.items():
        race, _ = Race.objects.get_or_create(
            name=player_info["race"]["name"],
            defaults={
                "description": player_info["race"]["description"],
            },
        )

        for skill in player_info["race"]["skills"]:
            _, _ = Skill.objects.get_or_create(
                name=skill["name"],
                defaults={
                    "bonus": skill["bonus"],
                    "race": race,
                },
            )

        if player_info["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=player_info["guild"]["name"],
                defaults={
                    "description": player_info["guild"]["description"],
                },
            )
        else:
            guild = None

        _, _ = Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": player_info["email"],
                "bio": player_info["bio"],
                "race": race,
                "guild": guild,
                "created_at": timezone.now(),
            },
        )


if __name__ == "__main__":
    main()
