import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for key, value in players.items():
        name = key
        email = value["email"]
        bio = value["bio"]
        race = value["race"]
        skills = race["skills"]
        guild = value["guild"]

        race_obj = Race.objects.get_or_create(
            name=race.get("name"),
            description=race.get("description")
        )[0]
        if guild is not None:
            guild_obj = Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
            )[0]
        else:
            guild_obj = None

        # Player creation
        Player.objects.get_or_create(
            nickname=name,
            email=email,
            bio=bio,
            race=race_obj,
            guild=guild_obj,
        )
        # Skills creation
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race_obj,
            )


if __name__ == "__main__":
    main()
