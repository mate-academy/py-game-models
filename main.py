import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as input_file:
        players = json.load(input_file)
    for username, player_data in players.items():
        race_data = player_data["race"]
        race, boolean = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data.get("description", "")
        )

        for skill in race_data.get('skills', []):
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        guild_data = player_data["guild"]
        if guild_data:
            guild, boolean = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data.get("description", "")
            )
        else:
            guild = None

        Player.objects.get_or_create(nickname=username,
                                     email=player_data["email"],
                                     bio=player_data["bio"],
                                     race=race,
                                     guild=guild
                                     )


if __name__ == "__main__":
    main()
