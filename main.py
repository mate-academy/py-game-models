import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_data:
        players = json.load(players_data)
    for nickname, player_value in players.items():

        email, bio, race, guild = player_value.values()

        race_name, description, skills = race.values()

        race, is_present = Race.objects.get_or_create(
            name=race_name,
            description=description,
        )

        if not is_present:
            for skill in skills:
                Skill.objects.get_or_create(**skill, race=race)

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
