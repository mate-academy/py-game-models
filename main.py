import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def get_or_create_model_instance(
        model: Race | Guild,
        data_filter: dict,
        creation_data: dict
) -> Race | Guild:
    if not model.objects.filter(**data_filter).exists():
        instance = model.objects.create(**creation_data)
    else:
        instance = model.objects.get(**data_filter)
    return instance


def create_skills(skills_data: list[dict], race_object: Race) -> list:
    created_skills = []
    for skill in skills_data:
        if not Skill.objects.filter(
                name=skill.get("name"),
                race=race_object
        ).exists():
            new_skill = Skill.objects.create(**skill, race=race_object)
            created_skills.append(new_skill)
    return created_skills


def main() -> None:
    with open("players.json") as file:
        players_data = json.load(file)

    for name in players_data:
        player = players_data[name]
        player_race = player["race"]
        player_skills = player_race["skills"]
        player_guild = player["guild"]

        race_object: Race = get_or_create_model_instance(
            model=Race,
            data_filter={"name": player_race["name"]},
            creation_data={
                "name": player_race["name"],
                "description": player_race["description"]
            }
        )

        create_skills(
            skills_data=player_skills,
            race_object=race_object
        )

        guild_object = None
        if player_guild:
            guild_object = get_or_create_model_instance(
                model=Guild,
                data_filter={
                    "name": player_guild["name"]
                },
                creation_data={
                    "name": player_guild["name"],
                    "description": player_guild["description"]
                }
            )

        Player.objects.create(
            nickname=name,
            email=player["email"],
            bio=player["bio"],
            race=race_object,
            guild=guild_object
        )


if __name__ == "__main__":
    main()
