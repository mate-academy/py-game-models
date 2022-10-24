import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        data = json.load(f)

    def create_race(data: dict) -> Race:
        if not Race.objects.filter(name=data.get("name")).exists():
            return Race.objects.create(
                name=data.get("name"),
                description=data.get("description")
            )
        return Race.objects.get(name=data.get("name"))

    def create_skill(data: dict) -> None:
        for skill in data.get("skills"):
            if not Skill.objects.filter(name=skill.get("name")).exists():
                Skill.objects.create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=create_race(data)
                )

    def create_guild(data: dict) -> Guild | None:
        if data:
            if not Guild.objects.filter(name=data.get("name")).exists():
                return Guild.objects.create(
                    name=data.get("name"),
                    description=data.get("description")
                )
            return Guild.objects.get(name=data.get("name"))
        return None

    for name, info in data.items():
        race = create_race(info.get("race"))
        guild = create_guild(info.get("guild"))
        create_skill(info.get("race"))

        Player.objects.create(
            nickname=name,
            email=info.get("email"),
            bio=info.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
