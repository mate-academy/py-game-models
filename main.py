import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players_dict = json.load(players_file).items()

    for player, player_attr in players_dict:

        if not Race.objects.filter(name=player_attr["race"]["name"]).exists():
            Race.objects.create(
                name=player_attr["race"]["name"],
                description=player_attr["race"]["description"]
            )

        for skill in player_attr["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                race = Race.objects.get(name=player_attr["race"]["name"])
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        if player_attr.get("guild") is not None:
            if not Guild.objects.filter(
                    name=player_attr["guild"]["name"]
            ).exists():
                Guild.objects.create(
                    name=player_attr["guild"]["name"],
                    description=player_attr["guild"]["description"]
                )

            Player.objects.create(
                nickname=player,
                email=player_attr["email"],
                bio=player_attr["bio"],
                race=Race.objects.get(name=player_attr["race"]["name"]),
                guild=Guild.objects.get(name=player_attr["guild"]["name"])
            )
        else:
            Player.objects.create(
                nickname=player,
                email=player_attr["email"],
                bio=player_attr["bio"],
                race=Race.objects.get(name=player_attr["race"]["name"]),
            )


if __name__ == "__main__":
    main()
