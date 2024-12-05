import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_data:
        players = json.load(players_data)
    for nickname, player_value in players.items():

        email, bio, race_dict, guild = player_value.values()

        race, created = Race.objects.get_or_create(
            name=race_dict["name"],
            description=race_dict["description"]
        )

        if not created:
            for skill in race_dict["skills"]:
                Skill.objects.get_or_create(
                    **skill,
                    race=race
                )

        if guild:
            guild, _ = Guild.objects.get_or_create(**guild)

        Player.objects.create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
