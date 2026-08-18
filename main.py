import json

import init_django_orm  # noqa: F401

from db.models import Race, Guild, Skill, Player


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

        for player in players:
            email, bio, race, guild = players[player].values()
            name, description, skills = race.values()

            race_from_db, _ = Race.objects.get_or_create(
                name=name,
                description=description
            )

            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    defaults={
                        "bonus": skill["bonus"],
                        "race": race_from_db,
                    },
                )

            guild_from_db = None

            if guild is not None:
                guild_name, guild_description = guild.values()
                guild_from_db = Guild.objects.get_or_create(
                    name=guild_name,
                    description=guild_description
                )[0]

            Player.objects.get_or_create(
                nickname=player,
                defaults={
                    "race": race_from_db,
                    "guild": guild_from_db,
                    "email": email,
                    "bio": bio,
                }
            )


if __name__ == "__main__":
    main()
