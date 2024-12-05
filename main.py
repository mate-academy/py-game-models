import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild
from typing import Dict
import datetime


def load_json_file(file_path: str) -> Dict:
    with open(file_path, "r") as file:
        data_file = json.load(file)
    return data_file


def main() -> None:
    json_data = load_json_file("players.json")
    for nick_name, item in json_data.items():
        race, created = Race.objects.get_or_create(
            name=item["race"]["name"], description=item["race"]["description"]
        )

        for skill_info in item["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_info["name"], bonus=skill_info["bonus"], race=race
            )

        if item["guild"] is not None:
            guild, created = Guild.objects.get_or_create(
                name=item["guild"]["name"],
                description=item["guild"]["description"]
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=nick_name,
            email=item["email"],
            bio=item["bio"],
            create_at=datetime.datetime.today(),
            guild=guild,
            race=race,
        )


if __name__ == "__main__":
    main()
