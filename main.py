import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player in players:
        race, created = Race.objects.get_or_create(
            name=players.get(player).get("race").get("name"),
            description=players.get(player).get("race").get("description")
        )
        if players.get(player).get("race").get("skills"):
            for skill in players.get(player).get("race").get("skills"):
                Skill.objects.get_or_create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=race
                )

        Player.objects.get_or_create(
            nickname=player,
            email=players.get(player).get("email"),
            bio=players.get(player).get("bio"),
            race=race,
            guild=Guild.objects.get_or_create(
                name=players.get(player).get("guild").get("name"),
                description=players.get(player).get("guild").get("description")
            )[0] if players.get(player).get("guild") else None
        )


if __name__ == "__main__":
    main()
