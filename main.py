import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_data:
        players = json.load(players_data)

        for nick, data in players.items():
            race, created = Race.objects.get_or_create(
                name=data["race"]["name"],
                description=data["race"]["description"]
            )
            for skill in data["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race_id=race.id
                )
            guild = None
            if data["guild"]:
                guild, created = Guild.objects.get_or_create(
                    name=data["guild"]["name"],
                    description=data["guild"]["description"]
                )
            Player.objects.get_or_create(
                nickname=nick,
                email=data["email"],
                bio=data["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
