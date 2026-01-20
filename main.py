import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players_json_file = json.load(players_file)

    for player, values in players_json_file.items():
        race, _ = Race.objects.get_or_create(
            name=values["race"]["name"],
            description=values["race"]["description"]
        )

        guild = None
        guild_info = values.get("guild")
        if guild_info:
            guild, _ = Guild.objects.get_or_create(
                name=guild_info.get("name", ""),
                defaults={"description": guild_info.get("description")}
            )

        Player.objects.get_or_create(
            nickname=player,
            email=values["email"],
            bio=values["bio"],
            race=race,
            guild=guild,
        )
        for skill in values["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race,
            )


if __name__ == "__main__":
    main()
