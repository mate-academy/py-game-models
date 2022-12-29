import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json") as players_json_file:
        players_file = json.load(players_json_file)
        for name, value in players_file.items():
            if not Race.objects.filter(name=value["race"]["name"]):
                Race.objects.create(
                    name=value["race"]["name"],
                    description=value["race"]["description"]
                )

            if len(value["race"]["skills"]) >= 1:
                for skill in value["race"]["skills"]:
                    if not Skill.objects.filter(name=skill["name"]):
                        Skill.objects.create(
                            name=skill["name"],
                            bonus=skill["bonus"],
                            race_id=Race.objects.filter(
                                name=value["race"]["name"]
                            ).values_list("id", flat=True)
                        )

            if value["guild"] is not None and \
                    not Guild.objects.filter(
                        name=value["guild"]["name"]).exists():
                Guild.objects.create(
                    name=value["guild"]["name"],
                    description=value["guild"]["description"]
                )

            if not Player.objects.filter(nickname=name).exists():
                Player.objects.create(
                    nickname=name,
                    email=value["email"],
                    bio=value["bio"],

                    race_id=Race.objects.filter(
                        name=value["race"]["name"]
                    ).values_list("id", flat=True),

                    guild_id=Guild.objects.filter(
                        name=value["guild"]["name"]
                    ).values_list(
                        "id", flat=True
                    ) if value["guild"] is not None else None
                )


if __name__ == "__main__":
    main()
