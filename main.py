import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for name in data:
        race = Race.objects.get_or_create(
            name=data[name]["race"]["name"],
            description=data[name]["race"]["description"],
        )[0]

        if data[name]["race"].get("skills"):
            for skill in data[name]["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        if data[name].get("guild"):
            guild = Guild.objects.get_or_create(
                name=data[name]["guild"]["name"],
                description=(
                    data[name]["guild"]["description"]
                    if data[name]["guild"]["description"]
                    else None
                )
            )[0]

        Player.objects.create(
            nickname=name,
            email=data[name]["email"],
            bio=data[name]["bio"],
            race=race,
            guild=guild
        )
        guild = None


if __name__ == "__main__":
    main()
