import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json") as players_json_file:
        players_file = json.load(players_json_file)
        for name, info in players_file.items():
            race = info["race"]
            guild = info["guild"]
            if not Race.objects.filter(name=info["race"]["name"]):
                Race.objects.create(
                    name=race["name"],
                    description=race["description"]
                )

            if len(race["skills"]) >= 1:
                for skill in race["skills"]:
                    if not Skill.objects.filter(name=skill["name"]):
                        Skill.objects.create(
                            name=skill["name"],
                            bonus=skill["bonus"],
                            race_id=Race.objects.filter(
                                name=race["name"]
                            ).values_list("id", flat=True)
                        )

            if guild is not None and \
                    not Guild.objects.filter(
                        name=guild["name"]).exists():
                Guild.objects.create(
                    name=guild["name"],
                    description=guild["description"]
                )

            if not Player.objects.filter(nickname=name).exists():
                Player.objects.create(
                    nickname=name,
                    email=info["email"],
                    bio=info["bio"],

                    race_id=Race.objects.filter(
                        name=race["name"]
                    ).values_list("id", flat=True),

                    guild_id=Guild.objects.filter(
                        name=guild["name"]
                    ).values_list(
                        "id", flat=True
                    ) if guild is not None else None
                )


if __name__ == "__main__":
    main()
