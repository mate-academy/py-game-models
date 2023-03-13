import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players_info = json.load(players_file)
    for player_name, player_info in players_info.items():
        race_name = player_info["race"]["name"]
        try:
            Race.objects.get_or_create(
                name=race_name,
                defaults={
                    "description": player_info["race"]["description"]
                }

            )
        except Race.DoesNotExist:
            Race.objects.create(
                name=race_name,
                description=player_info["race"]["description"]
            )
        for skill in player_info["race"]["skills"]:
            try:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    defaults={
                        "bonus": skill["bonus"],
                        "race": Race.objects.get(name=race_name)
                    }
                )
            except Skill.DoesNotExist:
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],                        race=Race.objects.get(name=race_name)
                )
        if isinstance(player_info["guild"], dict):
            guild_name = player_info["guild"]["name"]
            try:
                Guild.objects.get_or_create(
                    name=guild_name,
                    defaults={
                        "description": player_info["guild"]["description"]
                    }
                )
                if guild_name is None:
                    raise Guild.DoesNotExist
            except Guild.DoesNotExist:
                Guild.objects.create(
                    name=player_info["guild"]["name"],
                    description=player_info["guild"]["description"]
                )

        player_guild = Guild.objects.get(
            name=player_info["guild"]["name"]
        ) if isinstance(player_info["guild"], dict) else None
        try:
            Player.objects.get_or_create(
                nickname=player_name,
                defaults={
                    "email": player_info["email"],
                    "bio": player_info["bio"],
                    "race": Race.objects.get(name=player_info["race"]["name"]),
                    "guild": player_guild
                }
            )
        except Player.DoesNotExist:
            Player.objects.create(
                nickname=player_name,
                email=player_info["email"],
                bio=player_info["bio"],
                race=Race.objects.get(name=player_info["race"]["name"]),
                guild=player_guild
            )


if __name__ == "__main__":
    main()
