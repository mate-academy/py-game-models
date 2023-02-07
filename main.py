import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    # Open and load JSON file to "players" variable
    with open("players.json") as players_file:
        players = json.load(players_file)
        for nickname, info in players.items():
            race = info["race"]
            skills = info["race"]["skills"]
            guild = info["guild"]

            # Create Race objects if records not exist yet
            obj, created = Race.objects.get_or_create(
                name=race["name"],
                description=race["description"]
            )

            # Create Guild objects if records not exist yet
            if guild:
                obj, created = Guild.objects.get_or_create(
                    name=guild["name"],
                    description=guild["description"]
                )

            # # Create Skill objects if records not exist yet
            if skills:
                for skill in skills:
                    obj, created = Skill.objects.get_or_create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=Race.objects.get(name=race["name"])
                    )

            # # Create Player objects if records not exist yet
            obj, created = Player.objects.get_or_create(
                nickname=nickname,
                email=info["email"],
                bio=info["bio"],
                race=Race.objects.get(name=race["name"]),
                guild=Guild.objects.get(name=guild["name"]) if guild else None
            )


if __name__ == "__main__":
    main()
