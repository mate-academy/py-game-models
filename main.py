import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, info in data.items():
        race = info.get("race")
        if not Race.objects.filter(name=race.get("name")).exists():
            Race.objects.create(
                name=race.get("name"),
                description=race.get("description")
            )

        skills = race.get("skills")
        for skill in skills:
            if not Skill.objects.filter(name=skill.get("name")).exists():
                Skill.objects.create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=Race.objects.filter(name=race.get("name")).get()
                )
        if info.get("guild"):
            guild = info.get("guild")
            if not Guild.objects.filter(name=guild.get("name")).exists():
                Guild.objects.create(
                    name=guild.get("name"),
                    description=guild.get("description")
                )

        race_id = race = Race.objects.filter(name=race.get("name")).get()
        guild_id = (
            Guild.objects.filter(name=guild.get("name")).get()
            if info.get("guild") else None)

        Player.objects.create(
            nickname=nickname,
            email=info.get("email"),
            bio=info.get("bio"),
            race=race_id,
            guild=guild_id,
        )


if __name__ == "__main__":
    main()
