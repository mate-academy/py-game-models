import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "rb") as file:
        whole_data = json.load(file)

    for data in whole_data:

        email = whole_data[data].get("email")
        bio = whole_data[data].get("bio")

        race_name = whole_data[data]["race"].get("name")

        race_des = whole_data[data]["race"].get("description")

        skills = whole_data[data]["race"].get("skills")

        guild = whole_data[data].get("guild")

        new_race, created = Race.objects.get_or_create(
            name=race_name,
            description=race_des
        )

        if skills is not None:
            for skill in skills:

                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=new_race
                )

        if guild is not None:
            guild, created = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )

        Player.objects.get_or_create(
            nickname=data,
            email=email,
            bio=bio,
            race=new_race,
            guild=guild
        )


if __name__ == "__main__":
    main()
