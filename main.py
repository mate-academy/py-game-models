import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)

    for player, info in players.items():
        guild_info = info["guild"]

        race_info = info["race"]

        guild = Guild.objects.get_or_create(
            name=guild_info["name"],
            description=guild_info["description"],
        )if guild_info else None

        race = Race.objects.get_or_create(
            name=race_info["name"],
            description=race_info["description"]
        )

        for skill in race_info["skills"]:
            Skill.objects.get_or_create(name=skill["name"],
                                        bonus=skill["bonus"],
                                        race_id=race[0].id)

        guild_id = guild[0].id if guild_info else None

        Player.objects.get_or_create(nickname=player,
                                     email=info["email"],
                                     bio=info["bio"],
                                     race_id=race[0].id,
                                     guild_id=guild_id)


if __name__ == "__main__":
    main()
