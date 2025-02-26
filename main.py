import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        json_data = json.load(file)

    for player in json_data:
        player_info = json_data[player]
        Race.objects.get_or_create(
            name=player_info["race"]["name"],
            description=player_info["race"]["description"]
        )
        if player_info["guild"] is not None:
            Guild.objects.get_or_create(
                name=player_info["guild"]["name"],
                description=player_info["guild"]["description"]
            )
        guild_name = player_info["guild"]
        guild_id = Guild.objects.get(
            name=guild_name["name"]).id if guild_name else None
        race_id = Race.objects.get(name=player_info["race"]["name"]).id
        Player.objects.get_or_create(
            nickname=player,
            email=player_info["email"],
            bio=player_info["bio"],
            race_id=race_id,
            guild_id=guild_id
        )
        for skill in player_info["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race_id=race_id
            )


if __name__ == "__main__":
    main()
