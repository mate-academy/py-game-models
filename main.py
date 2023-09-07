import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for nickname, info in players.items():
        email = info["email"]
        bio = info["bio"]
        race = info["race"]
        guild = info.get("guild")

        if Race.objects.filter(name=race["name"]).exists():
            player_race = Race.objects.get(name=race["name"])
        else:
            player_race = Race.objects.create(
                name=race["name"],
                description=race.get("description", "")
            )
            for skill in race["skills"]:
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=player_race
                )

        if guild:
            if Guild.objects.filter(name=guild["name"]).exists():
                player_guild = Guild.objects.get(name=guild["name"])
            else:
                player_guild = Guild.objects.create(
                    name=guild["name"],
                    description=guild.get("description")
                )
        else:
            player_guild = None

        Player.objects.create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=player_race,
            guild=player_guild
        )


if __name__ == "__main__":
    main()
