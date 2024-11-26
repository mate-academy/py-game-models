import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_info = json.load(file)
        for nickname, player_info in players_info.items():
            race_info = player_info["race"]
            guild_info = player_info["guild"]
            Race.objects.get_or_create(
                name=race_info["name"],
                description=race_info["description"]
            )
            for skill in race_info["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(name=race_info["name"])
                )
            if guild_info:
                Guild.objects.get_or_create(
                    name=guild_info["name"],
                    description=guild_info["description"]
                )
            guild_instance = Guild.objects.get(
                name=guild_info["name"]
            ) if guild_info else None
            Player.objects.create(
                nickname=nickname,
                email=player_info["email"],
                bio=player_info["bio"],
                race=Race.objects.get(name=race_info["name"]),
                guild=guild_instance
            )


if __name__ == "__main__":
    main()
