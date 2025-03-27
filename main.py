import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:

    with open("players.json") as file_load:
        json_load = json.load(file_load)
        for name, data in json_load.items():
            race, _ = Race.objects.get_or_create(
                name=data["race"]["name"],
                description=data["race"]["description"]
            )
            for name_bonus in data["race"]["skills"]:
                skill, _ = Skill.objects.get_or_create(
                    name=name_bonus["name"],
                    bonus=name_bonus["bonus"],
                    race=race
                )
            guild_data = data["guild"]
            if data["guild"]:
                guild, _ = Guild.objects.get_or_create(
                    name=data["guild"]["name"],
                    description=guild_data.get("description")
                )
            else:
                guild = None
            Player.objects.get_or_create(
                nickname=name,
                email=data["email"],
                bio=data["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
