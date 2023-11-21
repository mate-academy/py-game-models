import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for user_name, user_data in data.items():
        race = user_data.get("race")
        guild = user_data.get("guild")
        skills = race.get("skills")

        if race:
            race, created = Race.objects.get_or_create(
                name=race.get("name"),
                description=race.get("description")
            )

        if guild:
            guild, created = Guild.objects.get_or_create(
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

        Player.objects.create(
            nickname=user_name,
            email=user_data.get("email"),
            bio=user_data.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
