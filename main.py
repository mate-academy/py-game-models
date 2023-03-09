import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for player_name, player_info in data.items():
        race = player_info.get("race")
        skills = player_info.get("race")["skills"]
        guild = player_info.get("guild")

        if Race.objects.filter(name=race["name"]).exists():
            race = Race.objects.get(name=race["name"])
        else:
            race = Race.objects.create(name=race["name"],
                                       description=race["description"])

        for skill in skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                skill = Skill.objects.create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=race)
            else:
                Skill.objects.get(name=skill["name"])

        if guild:
            if Guild.objects.filter(name=guild["name"]).exists():
                guild = Guild.objects.get(name=guild["name"])
            else:
                guild = Guild.objects.create(
                    name=guild["name"],
                    description=guild["description"]
                )
        else:
            guild = None

        Player.objects.create(
            nickname=player_name,
            email=player_info.get("email"),
            bio=player_info.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
