import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players:
        all_players = json.load(players)

    for player_name, player_info in all_players.items():
        race = player_info["race"]
        skills = race["skills"]
        guild = player_info["guild"]

        if guild is None:
            guild_inst = None
        elif not Guild.objects.filter(name=guild["name"]).exists():
            info_guild = guild["description"] if \
                guild["description"] is not None \
                else None
            Guild.objects.create(
                name=guild["name"],
                description=info_guild
            )
            guild_inst = Guild.objects.get(name=guild["name"])
        else:
            guild_inst = Guild.objects.get(name=guild["name"])

        if not Race.objects.filter(name=race["name"]).exists():
            info_race = race["description"] if race["description"] else ""
            Race.objects.create(
                name=race["name"],
                description=info_race
            )

        race_inst = Race.objects.get(name=race["name"])

        for skill in skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_inst
                )

        Player.objects.create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race_inst,
            guild=guild_inst,
        )


if __name__ == "__main__":
    main()
