import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def load_players(file_path: str) -> dict:
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def main() -> None:
    path_to_file = "players.json"
    data_players = load_players(path_to_file)

    for key, value in data_players.items():
        print(f"key: {key}")

        Race.objects.get_or_create(
            name=value["race"]["name"],
            description=value["race"]["description"]
        )

        race_id_elf = Race.objects.get(name="elf")
        race_id_human = Race.objects.get(name="human")

        skills = value["race"]["skills"]
        if len(skills):
            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race_id=race_id_elf.id
                )

        if value["guild"]:
            guild_instance, created = Guild.objects.get_or_create(
                name=value["guild"]["name"],
                description=value["guild"]["description"]
            )

            Player.objects.create(
                nickname=key,
                email=value["email"],
                bio=value["bio"],
                race=(
                    race_id_elf
                    if value["race"]["name"] == "elf"
                    else race_id_human
                ),
                guild=guild_instance
            )


if __name__ == "__main__":
    main()
