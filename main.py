import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def get_or_create_race(player: dict) -> Race:
    race_inst, created = Race.objects.get_or_create(
        name=player["race"]["name"],
        defaults={"description": player["race"]["description"]}
    )
    return race_inst


def create_player_skills(player: dict) -> None:
    race_data = get_or_create_race(player)
    for skill in player["race"]["skills"]:
        Skill.objects.get_or_create(
            name=skill["name"],
            defaults={
                "bonus": skill["bonus"],
                "race": race_data
            }
        )


def get_or_create_guild(player: dict) -> Guild:
    guild = player.get("guild")
    if guild is not None:
        guild_inst, created = Guild.objects.get_or_create(
            name=player["guild"]["name"],
            defaults={"description": player["guild"]["description"]}
        )

    else:
        guild_inst = None

    return guild_inst


def get_or_create_player(players: dict) -> None:
    for player_name, player in players.items():
        Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": player["email"],
                "bio": player["bio"],
                "race": get_or_create_race(player),
                "guild": get_or_create_guild(player)
            }
        )


def main() -> None:

    with open("players.json", "r") as file:
        players = json.load(file)

    for player_name, player in players.items():
        create_player_skills(player)
        get_or_create_player(players)


if __name__ == "__main__":
    main()
