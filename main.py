import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json") as file:
        players = json.load(file)

    for player, info in players.items():
        email, bio, race, guild = info.values()
        skills = race.get("skills")

        race, flag = Race.objects.get_or_create(
            name=race.get("name"),
            description=race.get("description")
        )

        if guild:
            guild, flag = Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
            )

        if skills:
            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=race
                )

        Player.objects.get_or_create(
            nickname=player,
            email=email,
            bio=bio,
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
