import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)
    for name in players:

        player = players[name]

        if player.get("guild") is not None:
            guild, _ = Guild.objects.get_or_create(
                name=player["guild"].get("name"),
                description=player["guild"].get("description")
            )
        else:
            guild = None

        race, _ = Race.objects.get_or_create(
            name=player["race"].get("name"),
            description=player["race"].get("description")
        )

        for skill in player["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race
            )

        Player.objects.get_or_create(
            nickname=name,
            email=player.get("email"),
            bio=player.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
