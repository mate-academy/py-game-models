import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players_info = json.load(f)

    for player, player_info in players_info.items():
        nickname = player
        email = player_info["email"]
        bio = player_info["bio"]
        player_race = player_info["race"]
        race_name = player_race["name"]
        race_description = player_race["description"]

        try:
            race = Race.objects.get(name=race_name)
        except Race.DoesNotExist:
            race = Race.objects.create(
                name=race_name,
                description=race_description
            )

        skills = player_race["skills"]
        for skill in skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        player_guild = player_info["guild"]
        if not player_guild:
            guild = None
        else:
            if Guild.objects.filter(name=player_guild["name"]).exists():
                guild = Guild.objects.get(name=player_guild["name"])
            else:
                guild = Guild.objects.create(
                    name=player_guild["name"],
                    description=player_guild["description"]
                )

        Player.objects.create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
