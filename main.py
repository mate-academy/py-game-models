import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players_dict = json.load(players_file).items()

    for player, player_attr in players_dict:
        Race.objects.get_or_create(
            name=player_attr["race"]["name"],
            description=player_attr["race"]["description"],
        )

        for skill in player_attr["race"]["skills"]:
            race = Race.objects.get(name=player_attr["race"]["name"])
            Skill.objects.get_or_create(
                name=skill["name"], bonus=skill["bonus"], race=race
            )

        if player_attr.get("guild") is not None:
            Guild.objects.get_or_create(
                name=player_attr.get("guild")["name"],
                description=player_attr.get("guild")["description"],
            )

        Player.objects.create(
            nickname=player,
            email=player_attr["email"],
            bio=player_attr["bio"],
            race=Race.objects.get(name=player_attr["race"]["name"]),
            guild=(
                Guild.objects.get(name=player_attr["guild"]["name"])
                if player_attr.get("guild") is not None
                else None
            ),
        )


if __name__ == "__main__":
    main()
