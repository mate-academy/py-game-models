import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player_nickname, player_info in players.items():
        race_object, _ = Race.objects.get_or_create(
            name=player_info["race"]["name"],
            defaults={
                "description": player_info["race"].get("description")
            }
        )

        for skill in player_info["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={
                    "bonus": skill["bonus"],
                    "race": race_object
                }
            )

        guild = player_info.get("guild")
        guild_object = None
        if guild:
            guild_object, _ = Guild.objects.get_or_create(
                name=guild["name"],
                defaults={
                    "description": guild.get("description")
                }
            )

        Player.objects.get_or_create(
            nickname=player_nickname,
            defaults={
                "email": player_info["email"],
                "bio": player_info["bio"],
                "race": race_object,
                "guild": guild_object
            }
        )


if __name__ == "__main__":
    main()
