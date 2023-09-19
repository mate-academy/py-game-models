import datetime
import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


with open("players.json", "r") as file:
    data = json.load(file)


def main() -> None:
    data1 = data.items()

    for i in data1:
        e5 = i[1].get("race").get("name")
        e6 = i[1].get("race").get("description")
        if not Race.objects.filter(name=e5).exists():
            race = Race.objects.create(
                name=e5,
                description=e6,
            )
            for skills_name in i[1].get("race").get("skills"):
                e7 = skills_name.get("name")
                e8 = skills_name.get("bonus")
                if not Skill.objects.filter(name=e7).exists():
                    Skill.objects.create(
                        name=e7,
                        bonus=e8,
                        race=race,
                    )

        if i[1].get("guild") is not None:
            e9 = i[1].get("guild").get("name")
            e10 = i[1].get("guild").get("description")
            if not Guild.objects.filter(name=e9).exists():
                guild = Guild.objects.create(
                    name=e9,
                    description=e10,
                )

        if i[1].get("guild") is None:
            Player.objects.create(
                nickname=i[0],
                email=i[1].get("email"),
                bio=i[1].get("bio"),
                race=race,
                guild=None,
                created_at=datetime.datetime.now(),
            )
        else:
            Player.objects.create(
                nickname=i[0],
                email=i[1].get("email"),
                bio=i[1].get("bio"),
                race=race,
                guild=guild,
                created_at=datetime.datetime.now(),
            )


if __name__ == "__main__":
    main()
