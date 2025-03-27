import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for key, value in players.items():
        race, _ = Race.objects.get_or_create(
            name=value["race"]["name"], defaults={
                "description": value["race"].get("description", "")
            })

        if value["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=value["guild"]["name"], defaults={
                    "description": value["guild"].get("description", "")
                })
        else:
            guild = None

        skills = []
        for skill_data in value["race"]["skills"]:
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race
                })
            skills.append(skill)

        Player.objects.get_or_create(
            nickname=key, defaults={
                "email": value["email"],
                "bio": value["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
