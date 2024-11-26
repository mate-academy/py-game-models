import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        player_data = json.load(file)
        for player, player_data in player_data.items():
            race_data = player_data["race"]
            guild_data = player_data["guild"]

            race, created = Race.objects.get_or_create(
                name=race_data["name"],
                description=race_data["description"]
            )

            for skill in race_data["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

            if guild_data:
                guild, created = Guild.objects.get_or_create(
                    name=guild_data["name"],
                    description=guild_data["description"]
                )
            else:
                guild = None

            Player.objects.get_or_create(
                nickname=player,
                email=player_data["email"],
                bio=player_data["bio"],
                guild=guild,
                race=race
            )


if __name__ == "__main__":
    main()
