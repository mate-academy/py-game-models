import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for nickname, player_data in data.items():

        # Getting or creating race
        race_info = player_data["race"]
        Race.objects.get_or_create(
            name=race_info["name"],
            description=race_info["description"]
        )

        # Getting or creating skill
        for skill in race_info["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=Race.objects.get(name=race_info["name"])
            )

        # Getting or creating guild
        guild_info = player_data["guild"]
        guild = None
        if guild_info:
            guild, created = Guild.objects.get_or_create(
                name=guild_info["name"],
                description=guild_info["description"],
            )

        # Creating player
        Player.objects.create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=Race.objects.get(name=race_info["name"]),
            guild=guild,
        )


if __name__ == "__main__":
    main()
