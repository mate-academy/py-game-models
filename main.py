import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_data_json:
        players_data_dict = json.load(players_data_json)

    for name, data in players_data_dict.items():
        race, created = Race.objects.get_or_create(
            name=data["race"]["name"],
            description=data["race"]["description"]
        )
        for skill_item in data["race"]["skills"]:
            skill, created = Skill.objects.get_or_create(
                name=skill_item["name"],
                bonus=skill_item["bonus"],
                race=race
            )

        if data.get("guild"):
            guild, created = Guild.objects.get_or_create(
                name=data["guild"]["name"],
                description=data["guild"]["description"]
            )
        else:
            guild = None

        player, created = Player.objects.get_or_create(
            nickname=name,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
