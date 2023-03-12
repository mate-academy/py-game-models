import init_django_orm  # noqa: F401
import json


from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players_info = json.load(players_file)
    for player_name, player_info in players_info.items():
        race_name = player_info["race"]["name"]
        if not Race.objects.filter(name=race_name):
            Race.objects.create(
                name=race_name,
                description=player_info["race"]["description"]
            )
            for skill in player_info["race"]["skills"]:
                if not Skill.objects.filter(name=skill["name"]):
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=Race.objects.get(name=race_name)
                    )

        guild_name = player_info["guild"]["name"]\
            if type(player_info["guild"]) == dict else None
        if not Guild.objects.filter(
                name=guild_name
        ) and guild_name is not None:
            Guild.objects.create(
                name=player_info["guild"]["name"],
                description=player_info["guild"]["description"]
            )
        if not Player.objects.filter(nickname=player_name):
            player_guild = Guild.objects.get(
                name=player_info["guild"]["name"]
            ) if type(player_info["guild"]) == dict else None
            Player.objects.create(
                nickname=player_name,
                email=player_info["email"],
                bio=player_info["bio"],
                race=Race.objects.get(name=player_info["race"]["name"]),
                guild=player_guild

            )


if __name__ == "__main__":
    main()
