import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_info:
        players = json.load(players_info)
        for key, value in players.items():
            person_email = value["email"]
            person_bio = value["bio"]
            if value["guild"] is not None:
                Guild.objects.get_or_create(
                    name=value["guild"]["name"],
                    description=value["guild"]["description"],
                )
                guild_name = Guild.objects.get(name=value["guild"]["name"])
            else:
                guild_name = None
            Race.objects.get_or_create(
                name=value["race"]["name"],
                description=value["race"]["description"],
            )
            for skill in value["race"]["skills"]:
                race_name = Race.objects.get(name=value["race"]["name"])
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_name
                )
            race_name = Race.objects.get(name=value["race"]["name"])
            Player.objects.get_or_create(
                nickname=key,
                email=person_email,
                bio=person_bio,
                race=race_name,
                guild=guild_name
            )


if __name__ == "__main__":
    main()
