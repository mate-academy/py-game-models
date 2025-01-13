import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for name, player_data in data.items():
        race, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            description=player_data["race"].get("description", "")
        )

        for skill_data in player_data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )

        guild = None
        if player_data["guild"]:
            guild, _ = Guild.objects.get_or_create(
            name=player_data["guild"]["name"],
            description=player_data["guild"].get("description")
            )

        Player.objects.get_or_create(
            nickname=name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
