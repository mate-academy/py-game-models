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
        skills = race["skills"]

        if race:
            player_race, _ = Race.objects.get_or_create(
                name=race["name"],
                description=race.get("description", "")
            )

        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=player_race
            )

        if guild:
            player_guild, _ = Guild.objects.get_or_create(
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
