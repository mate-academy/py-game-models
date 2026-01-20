import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as file:
        data = json.load(file)

    for player_name, other_info in data.items():

        player_email = other_info["email"]
        player_bio = other_info["bio"]
        player_race = other_info["race"]
        player_guild = other_info["guild"]
        player_skills = player_race["skills"]

        player_race = Race.objects.get_or_create(
            name=player_race["name"],
            description=player_race["description"]
        )[0]

        if player_guild:
            player_guild = Guild.objects.get_or_create(
                name=other_info["guild"]["name"],
                description=other_info["guild"]["description"]
            )[0]
        else:
            player_guild = None

        for skill in player_skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=player_race
            )

        Player.objects.create(
            nickname=player_name,
            email=player_email,
            bio=player_bio,
            race=player_race,
            guild=player_guild
        )


if __name__ == "__main__":
    main()
