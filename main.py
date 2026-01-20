import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as data_players:
        players = json.load(data_players)

    for nickname, player_data in players.items():
        email = player_data.get("email")
        bio = player_data.get("bio")

        race_name = player_data.get("race").get("name")
        race_description = player_data.get("race").get("description")
        race_skills = player_data.get("race").get("skills")

        race, _ = Race.objects.get_or_create(
            name=race_name,
            description=race_description
        )
        for skill in race_skills:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race
            )

        guild = player_data.get("guild")

        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
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
