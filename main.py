import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players:
        data_players = json.load(players)
    for nickname, characteristic in data_players.items():
        if not Player.objects.filter(nickname=nickname).exists():
            if not Race.objects.filter(
                    name=characteristic["race"]["name"]
            ).exists():
                race = Race.objects.create(
                    name=characteristic["race"]["name"],
                    description=characteristic["race"]["description"]
                )
            else:
                race = Race.objects.get(
                    name=characteristic["race"]["name"]
                )
            for skill in characteristic["race"]["skills"]:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race
                    )
            Player.objects.create(
                nickname=nickname,
                email=characteristic["email"],
                bio=characteristic["bio"],
                race=race
            )
            if characteristic["guild"]:
                if not Guild.objects.filter(
                        name=characteristic["guild"]["name"]
                ).exists():
                    guild = Guild.objects.create(
                        name=characteristic["guild"]["name"],
                        description=characteristic["guild"]["description"]
                    )
                else:
                    guild = Guild.objects.get(
                        name=characteristic["guild"]["name"]
                    )
                Player.objects.filter(nickname=nickname).update(guild=guild)


if __name__ == "__main__":
    main()
