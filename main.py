import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_info = json.load(file)

    for name, player_info in players_info.items():
        race = player_info["race"]
        if not Race.objects.filter(name=race["name"]).exists():
            players_race = Race.objects.create(name=race["name"], description=race["description"])
        else:
            players_race = Race.objects.get(name=race["name"])

            if player_info["race"]["skills"]:
                for skill in player_info["race"]["skills"]:
                    if not Skill.objects.filter(name=skill["name"]).exists():
                        Skill.objects.create(
                            name=skill["name"],
                            bonus=skill["bonus"],
                            race=players_race
                        )

        guild = player_info["guild"]
        if guild:
            if not Guild.objects.filter(name=guild["name"]).exists():
                players_guild = Guild.objects.create(name=guild["name"], description=guild["description"])
            else:
                players_guild = Guild.objects.get(name=guild["name"])
        else:
            players_guild = None

        Player.objects.create(
            nickname=name,
            email=player_info.get("email"),
            bio=player_info.get("bio"),
            race=players_race,
            guild=players_guild
        )


if __name__ == "__main__":
    main()
