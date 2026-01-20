import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    data = None
    with open("players.json", "r") as reader:
        data = json.load(reader)

    for nickname, player_data in data.items():
        if not Player.objects.filter(nickname=nickname).exists():
            race = player_data["race"]
            guild = player_data["guild"]

            if Race.objects.filter(name=race["name"]).exists():
                race = Race.objects.get(name=race["name"])
            else:
                race_skills = race.get("skills")
                race = Race.objects.create(
                    name=race["name"],
                    description=race["description"]
                )
                if race_skills:
                    for race_skill in race_skills:
                        Skill.objects.create(
                            name=race_skill["name"],
                            bonus=race_skill["bonus"],
                            race=race
                        )

            if guild:
                if Guild.objects.filter(name=guild["name"]).exists():
                    guild = Guild.objects.get(name=guild["name"])
                else:
                    guild = Guild.objects.create(
                        name=guild["name"],
                        description=guild["description"]
                    )

            Player.objects.create(
                nickname=nickname,
                email=player_data["email"],
                bio=player_data["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
