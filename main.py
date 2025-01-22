import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players_data = json.load(file)

    race_cache = {}
    skill_cache = {}

    for player in players_data:
        race_name = player["race"]["name"]
        race_description = player["race"].get("description", "")

        if race_name not in race_cache:
            race, created = Race.objects.get_or_create(name=race_name, defaults={"description": race_description})
            race_cache[race_name] = race
        else:
            race = race_cache[race_name]

        for skill_data in player["race"].get("skills", []):
            skill_name = skill_data["name"]
            skill_bonus = skill_data.get("bonus", "")

            if skill_name not in skill_cache:
                skill, created = Skill.objects.get_or_create(
                    name=skill_name,
                    defaults={"bonus": skill_bonus, "race": race}
                )
                skill_cache[skill_name] = skill


if __name__ == "__main__":
    main()
