import datetime
import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


with open("players.json", "r") as file:
    data = json.load(file)


def main() -> None:
    data_model = data.items()

    for component in data_model:
        if not Race.objects.filter(
                name=component[1].get("race").get("name")).exists(

        ):
            race = Race.objects.create(
                name=component[1].get("race").get("name"),
                description=component[1].get("race").get("description"),
            )
            for skills_name in component[1].get("race").get("skills"):
                name_skills = skills_name.get("name")
                bonus_skills = skills_name.get("bonus")
                if not Skill.objects.filter(name=name_skills).exists():
                    Skill.objects.create(
                        name=name_skills,
                        bonus=bonus_skills,
                        race=race,
                    )

        if component[1].get("guild") is not None:
            if not Guild.objects.filter(
                    name=component[1].get("guild").get("name")).exists(

            ):
                guild = Guild.objects.create(
                    name=component[1].get("guild").get("name"),
                    description=component[1].get("guild").get("description"),
                )

        if component[1].get("guild") is None:
            Player.objects.create(
                nickname=component[0],
                email=component[1].get("email"),
                bio=component[1].get("bio"),
                race=race,
                guild=None,
                created_at=datetime.datetime.now(),
            )
        else:
            Player.objects.create(
                nickname=component[0],
                email=component[1].get("email"),
                bio=component[1].get("bio"),
                race=race,
                guild=guild,
                created_at=datetime.datetime.now(),
            )


if __name__ == "__main__":
    main()
