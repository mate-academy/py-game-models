import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        user_data = json.load(file)

    for player, data in user_data.items():

        race, _ = Race.objects.get_or_create(
            name=data["race"]["name"],
            defaults={"description": data["race"]["description"]})

        guild = None
        if data["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=data["guild"]["name"],
                defaults={"description": data["guild"]["description"]}
            )
        if data["race"]["skills"] != []:
            for skill in data["race"]["skills"]:
                skill_details, _ = Skill.objects.get_or_create(
                    name=skill["name"],
                    defaults={"bonus": skill["bonus"],
                              "race": race})

        Player.objects.get_or_create(
            nickname=player,
            defaults={"email": data["email"],
                      "bio": data["bio"],
                      "race": race,
                      "guild": guild})


if __name__ == "__main__":
    main()
