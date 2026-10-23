import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as players_info:
        players_info = json.load(players_info)
        for player in players_info:
            Race.objects.get_or_create(
                name=players_info[player]["race"]["name"],
                description=players_info[player]["race"]["description"],
            )

            for skill in players_info[player]["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(
                        name=players_info[player]["race"]["name"]
                    )
                )

            guild_data = players_info[player].get("guild")

            if guild_data and guild_data.get("name"):
                Guild.objects.get_or_create(
                    name=guild_data["name"],
                    defaults={"description": guild_data.get("description", "")}
                )

            if guild_data and guild_data.get("name"):
                guild = Guild.objects.filter(name=guild_data["name"]).first()
            else:
                guild = None

            Player.objects.create(
                nickname=player,
                email=players_info[player]["email"],
                bio=players_info[player]["bio"],
                race=Race.objects.get(
                    name=players_info[player]["race"]["name"]
                ),
                guild=guild
            )


if __name__ == "__main__":
    main()
