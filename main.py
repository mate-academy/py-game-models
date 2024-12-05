import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players_info = json.load(players_file)
    for player_name, player_info in players_info.items():
        race_name = player_info["race"]["name"]
        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={
                "description": player_info["race"]["description"]
            }
        )
        for skill in player_info["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={
                    "bonus": skill["bonus"],
                    "race": race
                }
            )
        if isinstance(player_info["guild"], dict):
            guild_name = player_info["guild"]["name"]
            player_guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={
                    "description": player_info["guild"]["description"]
                }
            )
        else:
            player_guild = None
        Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": player_info["email"],
                "bio": player_info["bio"],
                "race": race,
                "guild": player_guild
            }
        )


if __name__ == "__main__":
    main()
