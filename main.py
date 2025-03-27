import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        player_info = json.load(file)

    for nickname, player_data in player_info.items():
        if player_data["race"]:
            race, race_create = Race.objects.get_or_create(
                name=player_data["race"]["name"],
                description=player_data["race"]["description"]
            )
        for player_skill in player_data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=player_skill["name"],
                bonus=player_skill["bonus"],
                race=race
            )
        guild = player_data["guild"]
        if guild:
            guild, guild_creat = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
