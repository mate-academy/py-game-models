import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
from json import load


def main() -> None:
    data = []

    with open("players.json", "r") as file:
        data = load(file)

    for nickname, item in data.items():
        race = item.get("race")
        guild = item.get("guild")
        skills = race.get("skills")

        race, created = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"],
        )

        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race,
            )

        if guild:
            guild, created = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"],
            )

        Player.objects.get_or_create(
            nickname=nickname,
            email=item["email"],
            bio=item["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
