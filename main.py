import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_info:
        players_data = json.load(players_info)
        for nickname, player_data in players_data.items():
            person_email = player_data["email"]
            person_bio = player_data["bio"]
            if player_data["guild"] is not None:
                Guild.objects.get_or_create(
                    name=player_data["guild"]["name"],
                    description=player_data["guild"]["description"],
                )
                guild_name = Guild.objects.get(
                    name=player_data["guild"]["name"]
                )
            else:
                guild_name = None
            Race.objects.get_or_create(
                name=player_data["race"]["name"],
                description=player_data["race"]["description"],
            )
            for skill in player_data["race"]["skills"]:
                race_name = Race.objects.get(name=player_data["race"]["name"])
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_name
                )
            race_name = Race.objects.get(name=player_data["race"]["name"])
            Player.objects.create(
                nickname=nickname,
                email=person_email,
                bio=person_bio,
                race=race_name,
                guild=guild_name
            )


if __name__ == "__main__":
    main()
