import json

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    global guild, race
    with open("players.json", "r") as source:
        players_data = json.load(source)

    for player_name, info in players_data.items():
        info_race = info["race"]
        if not Race.objects.filter(name=info_race["name"]).exists():
            race = Race.objects.create(
                name=info_race["name"],
                description=info_race["description"],
            )

        info_skills = info_race["skills"]
        for skill in info_skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        info_guild = info["guild"]
        if info_guild:
            if not Guild.objects.filter(name=info_guild["name"]).exists():
                guild = Guild.objects.create(
                    name=info_guild["name"],
                    description=info_guild["description"],
                )
        else:
            guild = None

        player = players_data[player_name]
        Player.objects.create(
            nickname=player_name,
            email=player["email"],
            bio=player["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
