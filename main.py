import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player_name, fields in players.items():
        guild, race = None, None

        if fields["race"]:
            race, _ = Race.objects.get_or_create(
                name=fields["race"]["name"],
                description=fields["race"]["description"],
            )

        if fields["race"]["skills"]:
            for skill in fields["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(name=fields["race"]["name"]),
                )

        if fields["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=fields["guild"]["name"],
                description=fields["guild"]["description"],
            )

        Player.objects.create(
            nickname=player_name,
            email=fields["email"],
            bio=fields["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
