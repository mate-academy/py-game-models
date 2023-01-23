import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        info = json.load(file)

    for player_nickname, data in info.items():
        if not Race.objects.filter(name=data["race"]["name"]).exists():
            Race.objects.create(
                name=data["race"]["name"],
                description=data["race"]["description"]
            )
        race_from_data = Race.objects.get(name=data["race"]["name"])

        for skill in data["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_from_data
                )
        if data["guild"]:
            if not Guild.objects.filter(name=data["guild"]["name"]).exists():
                Guild.objects.create(
                    name=data["guild"]["name"],
                    description=data["guild"]["description"]
                )
            guild_from_data = Guild.objects.get(name=data["guild"]["name"])
        else:
            guild_from_data = None

        if not Player.objects.filter(nickname=player_nickname).exists():
            Player.objects.create(
                nickname=player_nickname,
                email=data["email"],
                bio=data["bio"],
                race=race_from_data,
                guild=guild_from_data
            )


if __name__ == "__main__":
    main()
