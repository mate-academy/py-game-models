import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for player, data in players.items():
        race_data = data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]}
        )

        for skill_data in race_data["skills"]:
            skill, _ = Skill.objects.get_or_create(
                race=race,
                name=skill_data["name"],
                defaults={"bonus": skill_data["bonus"]}
            )

        guild = None
        if data["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=data["guild"]["name"],
                defaults={"description": data["guild"]["description"]}
            )

        Player.objects.get_or_create(
            nickname=player,
            defaults={"email": data["email"],
                      "bio": data["bio"],
                      "race": race,
                      "guild": guild},
        )


if __name__ == "__main__":
    main()
