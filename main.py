import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        gamers = json.load(file)

    for gamer, params in gamers.items():
        guild = params.get("guild")
        Player.objects.create(
            nickname=gamer,
            email=params.get("email"),
            bio=params.get("bio"),
            race=Race.objects.get_or_create(
                name=params.get("race").get("name"),
                description=params.get("race").get("description")
            )[0],
            guild=None if not guild else Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
            )[0]
        )

        skills = params.get("race").get("skills")
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=Race.objects.get_or_create(
                    name=params.get("race").get("name"),
                    description=params.get("race").get("description")
                )[0]
            )


if __name__ == "__main__":
    main()
