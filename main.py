import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        json_data = json.load(file)

    for player in json_data:
        player_info = json_data[player]
        if Race.objects.filter(
                name=player_info["race"]["name"]
        ):
            pass
        else:
            Race.objects.create(
                name=player_info["race"]["name"],
                description=player_info["race"]["description"]
            )
        if player_info["guild"] is not None:
            if Guild.objects.filter(
                    name=player_info["guild"]["name"]
            ):
                pass
            else:
                Guild.objects.create(
                    name=player_info["guild"]["name"],
                    description=player_info["guild"]["description"]
                )
        guild_id = Guild.objects.filter(
            name=player_info["guild"]["name"]
        ).values("id") if player_info["guild"] else None
        race_id = Race.objects.filter(
            name=player_info["race"]["name"]
        ).values("id")
        if Player.objects.filter(nickname=player):
            pass
        else:
            Player.objects.create(
                nickname=player,
                email=player_info["email"],
                bio=player_info["bio"],
                race_id=race_id,
                guild_id=guild_id
            )
        for skill in player_info["race"]["skills"]:
            if Skill.objects.filter(name=skill["name"]):
                pass
            else:
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race_id=race_id
                )


if __name__ == "__main__":
    main()
