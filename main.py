import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open('players.json', 'r') as file:
        data = json.load(file)
        for player_data in data:
            Player.objects.create(
                nickname=player_data["nickname"],
                email=player_data["email"],
                bio=player_data.get("bio", ""),
                race=Race.objects.get(name=player_data["race"]),
                guild=Guild.objects.get(name=player_data.get("guild", "Default Guild"))
            )


if __name__ == "__main__":
    main()
