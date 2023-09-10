import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        players = json.load(f)

    for name, characteristics in players.items():

        race_alias = characteristics["race"]

        if not Race.objects.filter(
                name=race_alias["name"]
        ).exists() and race_alias:
            race_to_create = Race.objects.create(
                name=race_alias["name"],
                description=race_alias["description"]
            )
        else:
            race_to_create = Race.objects.get(
                name=characteristics["race"]["name"]
            )

        skills_alias = characteristics["race"]["skills"]

        for name_skill in skills_alias:
            if not Skill.objects.filter(
                    name=name_skill["name"]
            ).exists() and name_skill:
                Skill.objects.create(
                    name=name_skill["name"],
                    bonus=name_skill["bonus"],
                    race=race_to_create
                )

        guild_alias = characteristics["guild"]
        if guild_alias:
            if not Guild.objects.filter(
                    name=guild_alias["name"]
            ).exists() and guild_alias:
                guild_to_create = Guild.objects.create(
                    name=guild_alias["name"],
                    description=guild_alias["description"]
                )
            else:
                guild_to_create = Guild.objects.get(name=guild_alias["name"])
        else:
            guild_to_create = None

        Player.objects.create(
            nickname=name,
            email=characteristics["email"],
            bio=characteristics["bio"],
            race=race_to_create,
            guild=guild_to_create
        )


if __name__ == "__main__":
    main()
