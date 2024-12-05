import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for nick_name_data, item in players_data.items():
        race, created = Race.objects.get_or_create(
            name=item["race"]["name"],
            description=item["race"]["description"]
        )
        for skill_info in item["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_info["name"],
                bonus=skill_info["bonus"],
                race=race
            )
        if item["guild"] is not None:
            guild, created = Guild.objects.get_or_create(
                name=item["guild"]["name"],
                description=item["guild"]["description"]
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=nick_name_data,
            email=item["email"],
            bio=item["bio"],
            guild=guild,
            race=race
        )


if __name__ == "__main__":
    main()
