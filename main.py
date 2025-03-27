import init_django_orm  # noqa: F401
import json
import datetime

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players_data = json.load(players_file)

    for player, data in players_data.items():
        Race.objects.get_or_create(
            name=data["race"]["name"],
            description=data["race"]["description"]
        )

        if len(players_data[player]["race"]["skills"]) != 0:
            for skill in data["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(
                        name=data["race"]["name"]
                    )
                )

        if data["guild"] is not None:
            Guild.objects.get_or_create(
                name=data["guild"]["name"],
                description=data["guild"]["description"]
            )

        if not Player.objects.filter(nickname=player).exists():
            Player.objects.create(
                nickname=player,
                email=data["email"],
                bio=data["bio"],
                race=Race.objects.get(
                    name=data["race"]["name"]
                ),
                guild=Guild.objects.get(
                    name=data["guild"]["name"])
                if data["guild"] else None,
                created_at=datetime.datetime.now()
            )


if __name__ == "__main__":
    main()
