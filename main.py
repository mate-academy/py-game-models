import init_django_orm  # noqa: F401
import json
import datetime

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players_data = json.load(players_file)

    for player in players_data:
        Race.objects.get_or_create(
            name=players_data[player]["race"]["name"],
            description=players_data[player]["race"]["description"]
        )

        if len(players_data[player]["race"]["skills"]) != 0:
            for skill in players_data[player]["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(
                        name=players_data[player]["race"]["name"]
                    )
                )

        if players_data[player]["guild"] is not None:
            Guild.objects.get_or_create(
                name=players_data[player]["guild"]["name"],
                description=players_data[player]["guild"]["description"]
            )

        if not Player.objects.filter(nickname=player).exists():
            Player.objects.create(
                nickname=player,
                email=players_data[player]["email"],
                bio=players_data[player]["bio"],
                race=Race.objects.get(
                    name=players_data[player]["race"]["name"]
                ),
                guild=Guild.objects.get(
                    name=players_data[player]["guild"]["name"])
                if players_data[player]["guild"] else None,
                created_at=datetime.datetime.now()
            )


if __name__ == "__main__":
    main()
