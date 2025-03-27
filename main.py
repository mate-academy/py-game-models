import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for nickname, value in players.items():

        race = value["race"]
        guild = value["guild"]
        skills = race["skills"]

        if race:
            race, _ = Race.objects.get_or_create(
                name=race["name"],
                description=race["description"]
            )

        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
            )

        if skills:
            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        Player.objects.create(
            nickname=nickname,
            email=value["email"],
            bio=value["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
