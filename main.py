import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        user_file = json.load(f)
        for person, person_info in user_file.items():
            race, _ = Race.objects.get_or_create(
                name=person_info["race"]["name"],
                description=person_info["race"]["description"]
            )

            for skill in person_info["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

            guild = None

            if person_info["guild"] is not None:
                guild, _ = Guild.objects.get_or_create(
                    name=person_info["guild"]["name"],
                    description=person_info["guild"]["description"]
                )

            Player.objects.get_or_create(
                nickname=person,
                email=person_info["email"],
                bio=person_info["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
