import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as source:
        data = json.load(source)

    for user in data:
        race = data[user].get("race")
        if race and not Race.objects.filter(name=race["name"]).exists():
            Race.objects.create(
                name=race["name"],
                description=race["description"]
            )
            skills = race["skills"]
            if skills:
                for skill in skills:
                    if not Skill.objects.filter(name=skill["name"]).exists():
                        Skill.objects.create(name=skill["name"],
                                             bonus=skill["bonus"],
                                             race_id=Race.objects.get(
                                                 name=race["name"]).id)

        guild = data[user].get("guild")
        if guild and not Guild.objects.filter(name=guild["name"]).exists():
            Guild.objects.create(
                name=guild["name"],
                description=guild["description"]
            )

        id_guild = guild
        if guild:
            id_guild = Guild.objects.get(
                name=guild["name"]
            ).id

        Player.objects.create(
            nickname=user,
            email=data[user].get("email"),
            bio=data[user].get("bio"),
            race_id=Race.objects.get(
                name=race["name"]
            ).id,
            guild_id=id_guild
        )


if __name__ == "__main__":
    main()
