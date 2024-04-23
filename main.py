import json

import init_django_orm  # noqa: F401
from db.models import Race, Guild, Players, Skill


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)
    for player_name, player_data in players_data.items():
        race_data = player_data["race"]
        skill_data = player_data["race"]["skills"]
        race, created = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"])
        for skill in skill_data:
            skill, created = Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race,
            )

        print(skill_data)
        race.save()

    #     skill_data = player_data["skills"]
    # race, created = Race.objects.get_or_create(
    #     name=player_data["name"],
    #     description=player_data["description"]
    #
    # skill, created = Skill.objects.get_or_create(
    #     name=skill_data["name"],
    #     bonus=skill_data["bonus"],
    #     race=race
    # )


if __name__ == "__main__":
    main()
