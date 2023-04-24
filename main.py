import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for name, info in players.items():
        guild = info.get("guild")
        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
            )

        race = info["race"]
        new_race, _ = Race.objects.get_or_create(
            name=race.get("name"),
            description=race.get("description")
        )

        skills = race["skills"]
        for skill in skills:
            Skill.objects.get_or_create(
                race=new_race,
                name=skill.get("name"),
                bonus=skill.get("bonus")
            )

        Player.objects.get_or_create(
            nickname=name,
            email=info.get("email"),
            bio=info.get("bio"),
            race=new_race,
            guild=guild
        )


if __name__ == "__main__":
    main()
