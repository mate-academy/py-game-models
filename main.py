import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player, player_info in players.items():
        race, _ = Race.objects.get_or_create(
            name=player_info["race"].get("name"),
            description=player_info["race"].get("description")
        )

        for skill in player_info["race"].get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race
            )

        guild = player_info.get("guild")
        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=player_info["guild"].get("name"),
                description=player_info["guild"].get("description")
            )

        Player.objects.get_or_create(
            nickname=player,
            email=player_info.get("email"),
            bio=player_info.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
