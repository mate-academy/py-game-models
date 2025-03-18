import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_data:
        players = json.load(players_data)

    for player, player_info in players.items():
        if Race.objects.filter(name=player_info["race"]["name"]):
            players_race = Race.objects.get(name=player_info["race"]["name"])
        else:
            players_race = Race.objects.create(
                name=player_info["race"]["name"],
                description=player_info["race"]["description"]
                if player_info["race"]["description"] else None)

        if not player_info["guild"]:
            players_guild = None

        else:
            if Guild.objects.filter(name=player_info["guild"]["name"]):
                players_guild = Guild.objects.get(
                    name=player_info["guild"]["name"]
                )
            else:
                players_guild = Guild.objects.create(
                    name=player_info["guild"]["name"],
                    description=player_info["guild"]["description"] if
                    player_info["guild"]["description"] else None
                )

        player_instance = Player.objects.create(
            nickname=player,
            email=player_info["email"],
            bio=player_info["bio"],
            race=players_race,
            guild=players_guild
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
