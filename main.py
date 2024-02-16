import init_django_orm  # noqa: F401

from datetime import datetime
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        data = json.load(f)

        for player, player_data in data.items():
            race, _ = Race.objects.get_or_create(
                name=player_data["race"]["name"],
                description=player_data["race"].get("description"))

            if player_data.get("guild"):
                guild, _ = Guild.objects.get_or_create(
                    name=player_data.get("guild").get("name"),
                    description=player_data["guild"].get("description"))
            else:
                guild = None

            for skill in player_data["race"]["skills"]:
                Skill.objects.get_or_create(name=skill["name"],
                                            bonus=skill["bonus"],
                                            race=race)

            Player.objects.create(
                nickname=player,
                email=player_data["email"],
                bio=player_data["bio"],
                race=race,
                guild=guild if guild else None,
                created_at=datetime.now())


if __name__ == "__main__":
    main()
