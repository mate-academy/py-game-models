import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("db/tests/players.json", "r") as file:
        players = json.load(file)

    for nickname, details in players.items():
        email = details["email"]
        bio = details["bio"]
        race = details["race"]
        guild = details["guild"]

        race_obj, _ = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"],
        )

        for skill in race["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                defaults={"race": race_obj},
            )

        guild_obj = Guild.objects.get_or_create(
            name=guild["name"],
            description=guild["description"],
        )[0] if guild else None

        Player.objects.create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race_obj,
            guild=guild_obj,
        )


if __name__ == "__main__":
    main()
