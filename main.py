import init_django_orm  # noqa: F401

from datetime import datetime
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        data = json.load(f)

        for key, value in data.items():
            race, _ = Race.objects.get_or_create(
                name=value["race"]["name"],
                description=value["race"].get("description"))

            if value["guild"]:
                guild, _ = Guild.objects.get_or_create(
                    name=value.get("guild").get("name"),
                    description=value["guild"].get("description"))
            else:
                guild = None

            for skill in value["race"]["skills"]:
                Skill.objects.get_or_create(name=skill["name"],
                                            bonus=skill["bonus"],
                                            race=race)

            Player.objects.create(
                nickname=key,
                email=value["email"],
                bio=value["bio"],
                race=race,
                guild=guild if guild else None,
                created_at=datetime.now())


if __name__ == "__main__":
    main()
