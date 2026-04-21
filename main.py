import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
    for nickname, data in players.items():
        race, _ = Race.objects.get_or_create(
            name=data["race"]["name"],
            defaults={
                "description": data["race"]["description"]
            }
        )
        skills_data = data["race"]["skills"]
        for skill_ in skills_data:
            skill, _ = Skill.objects.get_or_create(
                name=skill_["name"],
                race=race,
                defaults={
                    "bonus": skill_["bonus"],
                }
            )
        Player.objects.create(
            nickname=nickname,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=Guild.objects.get_or_create(
                name=data["guild"]["name"],
                defaults={
                    "description": data["guild"]["description"]
                }
            )[0] if data.get("guild") else None
        )


if __name__ == "__main__":
    main()
