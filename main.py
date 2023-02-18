import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_info = json.load(file)
        for player in players_info:
            race_info = players_info[player]["race"]
            guild_info = players_info[player]["guild"]
            if not Race.objects.filter(name=race_info["name"]).exists():
                Race.objects.create(
                    name=race_info["name"],
                    description=race_info["description"]
                )
                for skill in race_info["skills"]:
                    if not Skill.objects.filter(name=skill["name"]).exists():
                        Skill.objects.create(
                            name=skill["name"],
                            bonus=skill["bonus"],
                            race=Race.objects.get(name=race_info["name"])
                        )
            if guild_info:
                if not Guild.objects.filter(name=guild_info["name"]).exists():
                    Guild.objects.create(
                        name=guild_info["name"],
                        description=guild_info["description"]
                    )
            guild_instance = Guild.objects.get(
                name=guild_info["name"]
            ) if guild_info else None
            Player.objects.create(
                nickname=player,
                email=players_info[player]["email"],
                bio=players_info[player]["bio"],
                race=Race.objects.get(name=race_info["name"]),
                guild=guild_instance
            )


if __name__ == "__main__":
    main()
