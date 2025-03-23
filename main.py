import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        characters = json.load(file)

    for player_name, player_data in characters.items():

        race, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            description=player_data["race"]["description"]
        )

        for skill_info in player_data["race"]["skills"]:
            skill, _ = Skill.objects.get_or_create(
                name=skill_info["name"],
                bonus=skill_info["bonus"],
                race=race
            )

        guild = player_data.get("guild")
        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )

        Player.objects.get_or_create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
