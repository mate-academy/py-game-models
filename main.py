import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

        for nickname, player_info in data.items():

            race, created = Race.objects.get_or_create(
                name=player_info["race"]["name"],
                description=player_info["race"]["description"]
            )

            for skill in player_info["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

            guild = None
            if player_info["guild"]:
                guild, created = Guild.objects.get_or_create(
                    name=player_info["guild"]["name"],
                    description=player_info["guild"]["description"]
                )

            Player.objects.create(
                nickname=nickname,
                email=player_info["email"],
                bio=player_info["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
