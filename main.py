import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_data:
        players = json.load(players_data)

    for player, player_info in players.items():
        player_instance = Player.objects.create(
            nickname=player,
            email=player_info["email"],
            bio=player_info["bio"],
            race=Race.objects.get(name=player_info["race"]["name"])
            if Race.objects.filter(name=player_info["race"]["name"])
            else Race.objects.create(
                name=player_info["race"]["name"],
                description=player_info["race"]["description"] if
                player_info["race"]["description"] else None
            ),
            guild=None if not player_info["guild"] else
            (
                Guild.objects.get(name=player_info["guild"]["name"])
                if Guild.objects.filter(name=player_info["guild"]["name"])
                else Guild.objects.create(
                    name=player_info["guild"]["name"],
                    description=player_info["guild"]["description"]
                    if player_info["guild"]["description"] else None
                )),
        )
        for skill in player_info["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]):
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=player_instance.race
                )


if __name__ == "__main__":
    main()
