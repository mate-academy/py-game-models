import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as file:
        data = json.load(file)

    for player_name, information in data.items():
        race = information["race"]
        guild = information["guild"]

        race_ref, is_created_race = Race.objects.get_or_create(
            name=race["name"], description=race["description"]
        )

        skills = race["skills"]
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=Race.objects.get(name=race["name"])
            )
        email = information["email"]
        bio = information["bio"]

        if guild:
            guild_ref, is_created_guild = Guild.objects.get_or_create(
                name=guild["name"], description=guild["description"]
            )
            Player.objects.create(
                nickname=player_name,
                email=email,
                bio=bio,
                race=race_ref,
                guild=guild_ref
            )
        else:
            Player.objects.create(
                nickname=player_name,
                email=email,
                bio=bio,
                race=race_ref,
            )


if __name__ == "__main__":
    main()
