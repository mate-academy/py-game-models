import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        date = json.loads(f.read())

    def create_race(date: dict) -> Race:
        date = date.get("race")
        if not Race.objects.filter(name=date.get("name")).exists():
            Race.objects.create(
                name=date.get("name"),
                description=date.get("description")
            )
        return Race.objects.get(name=date.get("name"))

    def create_skill(date: dict) -> None:
        for skill in date.get("race").get("skills"):
            if not Skill.objects.filter(name=skill.get("name")).exists():
                Skill.objects.create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=create_race(date)
                )

    def create_guild(date: dict) -> Guild | None:
        if date.get("guild"):
            date = date.get("guild")
            if not Guild.objects.filter(name=date.get("name")).exists():
                Guild.objects.create(
                    name=date.get("name"),
                    description=date.get("description")
                )
            return Guild.objects.get(name=date.get("name"))
        return None

    for name, info in date.items():
        race = create_race(info)
        guild = create_guild(info)
        create_skill(info)

        Player.objects.create(
            nickname=name,
            email=info.get("email"),
            bio=info.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
