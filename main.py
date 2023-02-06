import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    # Open and load JSON file to "players" variable
    with open("players.json") as players_file:
        players = json.load(players_file)
        for player in players:
            race = players[player]["race"]
            skills = players[player]["race"]["skills"]
            guild = players[player]["guild"]
            # Create Race objects if records not exist yet
            if not Race.objects.filter(name=race["name"]).exists():
                Race.objects.create(
                    name=race["name"],
                    description=race["description"]
                )
            # Create Guild objects if records not exist yet
            if guild:
                if not Guild.objects.filter(name=guild["name"]).exists():
                    Guild.objects.create(
                        name=guild["name"],
                        description=guild["description"]
                    )
            # Create Skill objects if records not exist yet
            if skills:
                for skill in skills:
                    if not Skill.objects.filter(name=skill["name"]).exists():
                        Skill.objects.create(
                            name=skill["name"],
                            bonus=skill["bonus"],
                            race=Race.objects.get(name=race["name"])
                        )
            # Create Player objects if records not exist yet
            if not Player.objects.filter(nickname=player).exists():
                Player.objects.create(
                    nickname=player,
                    email=players[player]["email"],
                    bio=players[player]["bio"],
                    race=Race.objects.get(name=race["name"]),
                    guild=Guild.objects.get(
                        name=guild["name"]
                    ) if guild else None
                )


if __name__ == "__main__":
    main()
