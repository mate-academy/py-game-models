import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

        for nickname, info in data.items():

            race_obj, _ = Race.objects.get_or_create(
                name=info["race"]["name"],
                defaults={"description": info["race"].get("description", "")}
            )

            for skill in info["race"].get("skills", []):
                Skill.objects.get_or_create(
                    name=skill["name"],
                    defaults={
                        "bonus": skill.get("bonus", ""),
                        "race": race_obj
                    }
                )

            guild_data = info.get("guild")

            guild_obj = None
            if guild_data:
                guild_obj, _ = Guild.objects.get_or_create(
                    name=guild_data["name"],
                    defaults={"description": guild_data.get("description")}
                )

            Player.objects.get_or_create(
                nickname=nickname,
                defaults={
                    "email": info.get("email", ""),
                    "bio": info.get("bio", ""),
                    "race": race_obj,
                    "guild": guild_obj
                }
            )


if __name__ == "__main__":
    main()
