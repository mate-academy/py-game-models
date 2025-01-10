"""
Implement a function main() which will have the following logic:

Read data about players from players.json and add the corresponding entries to
the database. Note, that some guilds, races and skills are used for different
players. Create only one instance for each guild, race and skill, do not copy
them.

Note: It would be very useful to use the get_or_create() method here. We don't
prioritize performance for this task, so querying the database to check 
whether a row already exists is acceptable. There’s no need to use bulk_create
in this case, as it adds unnecessary complexity to the task.
"""

import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player_name, value in players.items():
        race = Race.objects.get_or_create(
            name=value["race"]["name"],
            description=value["race"]["description"],
        )[0]

        for skill in value["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race,
            )

        guild = None if not value["guild"] else Guild.objects.get_or_create(
            name=value["guild"]["name"],
            description=value["guild"]["description"],)[0]

        Player.objects.create(
            nickname=player_name,
            email=value["email"],
            bio=value["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
