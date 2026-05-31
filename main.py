import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for details in players.values():
        Race.objects.get_or_create(
            name=details["race"]["name"],
            description=details["race"]["description"],
        )

    for details in players.values():
        guild_info = details.get("guild")
        if guild_info:
            Guild.objects.get_or_create(
                name=guild_info["name"],
                description=guild_info["description"],
            )

    for details in players.values():
        race = Race.objects.get(name=details["race"]["name"])
        for skill in details["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race,
            )

    for nickname, details in players.items():
        race = Race.objects.get(name=details["race"]["name"])
        guild_info = details.get("guild")
        guild = (Guild.objects.get(name=guild_info["name"])
                 if guild_info else None)
        Player.objects.get_or_create(
            nickname=nickname,
            email=details["email"],
            bio=details["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
