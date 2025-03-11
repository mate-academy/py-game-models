import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as json_file:
        players_dict = json.load(json_file)

    for name, attributes in players_dict.items():
        guild = attributes.get("guild")

        if guild:
            guild, *_ = Guild.objects.get_or_create(
                name=guild["name"],
                defaults={"description": guild["description"]}
            )

        race, *_ = Race.objects.get_or_create(
            name=attributes["race"]["name"],
            defaults={"description": attributes["race"]["description"]}
        )

        for skills in attributes["race"]["skills"]:

            skill_obj, *_ = Skill.objects.get_or_create(
                name=skills["name"],
                defaults={"bonus": skills["bonus"], "race": race}
            )

        Player.objects.create(
            nickname=name,
            email=attributes["email"],
            bio=attributes["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
