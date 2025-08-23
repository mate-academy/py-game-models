import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for name, info in players.items():
        race_info = info["race"]

        race_obj, _ = Race.objects.get_or_create(
            name=race_info["name"],
            description=race_info.get("description")
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
                race=race_obj,
            )

        Player.objects.get_or_create(
            nickname=name, email=info["email"], bio=info["bio"],
            race=race_obj,
            guild=guild_obj,
        )


if __name__ == "__main__":
    main()
