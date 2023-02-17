import datetime
import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player in data:
        Race.objects.get_or_create(
            name=data[player]["race"]["name"],
            description=data[player]["race"]["description"]
        )

        if len(data[player]["race"]["skills"]) != 0:
            for skill in data[player]["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(name=data[player]["race"]["name"])
                )

        if data[player]["guild"] is not None:
            Guild.objects.get_or_create(
                name=data[player]["guild"]["name"],
                description=data[player]["guild"]["description"]
            )

        if not Player.objects.filter(nickname=player).exists():
            Player.objects.create(
                nickname=player,
                email=data[player]["email"],
                bio=data[player]["bio"],
                race=Race.objects.get(name=data[player]["race"]["name"]),
                guild=Guild.objects.get(
                    name=data[player]["guild"]["name"])
                if data[player]["guild"] else None,
                created_at=datetime.datetime.now()
            )


if __name__ == "__main__":
    main()

# if not Race.objects.filter(name=data[player]["race"]["name"]).exists():
#     race = Race.objects.create(
#         name=data[player]["race"]["name"],
#         description=data[player]["race"]["description"]
#     )
# else:
#     race = Race.objects.get(name=data[player]["race"]["name"])
#
# if len(data[player]["race"]["skills"]) != 0:
#     for skill in data[player]["race"]["skills"]:
#         if not Skill.objects.filter(name=skill["name"]).exists():
#             Skill.objects.create(
#                 name=skill["name"],
#                 bonus=skill["bonus"],
#                 race=race
#             )
#
# guild = None
# if data[player]["guild"] is not None:
#     if not Guild.objects.filter(
#             name=data[player]["guild"]["name"]
#     ).exists():
#         guild = Guild.objects.create(
#             name=data[player]["guild"]["name"],
#             description=data[player]["guild"]["description"]
#         )
#     else:
#         guild = Guild.objects.get(name=data[player]["guild"]["name"])
#
# if not Player.objects.filter(nickname=player).exists():
#     Player.objects.create(
#         nickname=player,
#         email=data[player]["email"],
#         bio=data[player]["bio"],
#         race=race,
#         guild=guild,
#         created_at=datetime.datetime.now()
#     )
