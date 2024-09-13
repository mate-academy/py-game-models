import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json", "r") as f:
        player_data = json.load(f)
        for information in player_data.values():
            race = information["race"]
            guild = information["guild"]
            guild_name = guild["name"] if guild else None
            guild_description = guild["description"] if guild else None
            player_name = "".join(information["email"].split("@")[0])

            race, created = Race.objects.get_or_create(
                name=race["name"],
                description=race["description"]
            )

            if guild is not None:
                guild, created = Guild.objects.get_or_create(
                    name=guild_name,
                    description=guild_description
                )
            if Guild is None:
                guild = None

            for skill in information["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

            Player.objects.create(
                nickname=player_name,
                email=information["email"],
                bio=information["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
