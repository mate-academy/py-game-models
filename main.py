import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player_name, model_data in data.items():
        race, _ = Race.objects.get_or_create(
            name=model_data["race"]["name"],
            description=model_data["race"]["description"]
        )
        guild = None

        if model_data.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=model_data["guild"].get("name"),
                description=model_data["guild"].get("description"))

        player, _ = Player.objects.get_or_create(
            nickname=player_name,
            email=model_data["email"],
            bio=model_data["bio"],
            race=race,
            guild=guild
        )

        skill_data = model_data["race"].get("skills")

        if skill_data:
            for skill in skill_data:
                skills, _ = Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )


if __name__ == "__main__":
    main()
