import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as data:
        players_data = json.load(data)

    for nickname, player_data in players_data.items():

        race_data = player_data["race"]
        if Race.objects.filter(name=race_data["name"]).exists():
            race = Race.objects.get(name=race_data["name"])
        else:
            race = Race.objects.create(
                name=race_data["name"],
                description=(race_data["description"]
                             if race_data["description"] else None)
            )

        if skills := race_data["skills"]:
            for skill in skills:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race
                    )

        guild_data = player_data["guild"] if player_data["guild"] else None
        guild = None
        if guild_data:
            if Guild.objects.filter(name=guild_data["name"]).exists():
                guild = Guild.objects.get(name=guild_data["name"])
            else:
                guild = Guild.objects.create(**guild_data)

        Player.objects.create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
