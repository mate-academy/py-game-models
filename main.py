import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

        for name, info in players.items():
            Race.objects.get_or_create(
                name=info["race"]["name"],
                description=info["race"].get("description")
            )
            guild_info = info.get("guild")
            guild_obj = None
            if guild_info:
                guild_obj, _ = Guild.objects.get_or_create(
                    name=guild_info["name"],
                    defaults={"description": guild_info.get("description")}
                )

            for skill in info["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"], bonus=skill["bonus"],
                    race=Race.objects.get(name=info["race"]["name"]),
                )

            Player.objects.get_or_create(
                nickname=name, email=info["email"], bio=info["bio"],
                race=Race.objects.get(name=info["race"]["name"]),
                guild=guild_obj,
            )


if __name__ == "__main__":
    main()
