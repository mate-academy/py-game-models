import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("db/tests/players.json", "r") as f:
        players_dict = json.load(f)

    for nickname, fields in players_dict.items():
        bio = fields["bio"]
        email = fields["email"]
        race = fields["race"]
        guild = fields["guild"]
        skills = race["skills"]

        race = Race.objects.get_or_create(
            name=race["name"], description=race["description"]
        )[0]

        guild = (
            Guild.objects.get_or_create(
                name=guild["name"], description=guild["description"]
            )[0]
            if guild
            else None
        )

        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"], bonus=skill["bonus"], race=race
            )

        Player.objects.create(
            nickname=nickname, email=email, bio=bio, race=race, guild=guild
        )


if __name__ == "__main__":
    main()
