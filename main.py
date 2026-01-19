import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)
        for player, data in players.items():

            player_race, created = Race.objects.get_or_create(
                name=data["race"]["name"],
                description=data["race"]["description"]
            )

            skills = data["race"]["skills"]
            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=player_race
                )

            player_guild = data["guild"] or None
            if player_guild:
                player_guild, created = Guild.objects.get_or_create(
                    name=player_guild["name"],
                    description=player_guild["description"]
                )

            Player.objects.create(
                nickname=player,
                email=data["email"],
                bio=data["bio"],
                race=player_race,
                guild=player_guild
            )


if __name__ == "__main__":
    main()
