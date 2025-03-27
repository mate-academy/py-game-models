import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)
    for nickname, ability in data.items():
        race, _ = Race.objects.get_or_create(
            name=ability["race"]["name"],
            description=ability["race"].get("description")
        )
        guild = None
        if ability.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=ability["guild"].get("name"),
                description=ability["guild"].get("description")
            )
        Player.objects.get_or_create(
            nickname=nickname,
            email=ability["email"],
            bio=ability["bio"],
            race=race,
            guild=guild
        )
        for skill in ability["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )


if __name__ == "__main__":
    main()
