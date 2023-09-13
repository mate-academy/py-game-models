import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        players = json.load(f)

    for name, characteristics in players.items():
        race_alias = characteristics["race"]
        race_to_create, _ = Race.objects.get_or_create(
            name=race_alias["name"],
            defaults={"description": race_alias["description"]}
        )

        skills_alias = characteristics["race"]["skills"]
        for name_skill in skills_alias:
            Skill.objects.get_or_create(
                name=name_skill["name"],
                defaults={"bonus": name_skill["bonus"], "race": race_to_create}
            )

        guild_alias = characteristics.get("guild")
        if guild_alias:
            guild_to_create, _ = Guild.objects.get_or_create(
                name=guild_alias["name"],
                defaults={"description": guild_alias["description"]}
            )
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
