import init_django_orm  # noqa: F401
from json import load
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = load(file)
    for key, value in data.items():
        race, created = Race.objects.get_or_create(
            name=value["race"]["name"],
            description=value["race"].get("description")
        )
        if value["guild"]:
            guild, created = Guild.objects.get_or_create(
                name=value["guild"].get("name"),
                description=value["guild"].get("description")
            )
        else:
            guild = None
        Player.objects.get_or_create(
            nickname=key,
            email=value["email"],
            bio=value["bio"],
            race=race,
            guild=guild
        )
        for skill in value["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )


if __name__ == "__main__":
    main()
