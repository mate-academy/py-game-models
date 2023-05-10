import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, info in data.items():
        race = info.get("race")
        race_id, _ = Race.objects.get_or_create(
            name=race.get("name"),
            description=race.get("description")
        )

        skills = race.get("skills")
        for skill in skills:
            skill_id, _ = Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=Race.objects.filter(name=race.get("name")).get()
            )
        if info.get("guild"):
            guild = info.get("guild")
            guild_id, _ = Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
            )
        else:
            guild_id = None

        Player.objects.create(
            nickname=nickname,
            email=info.get("email"),
            bio=info.get("bio"),
            race=race_id,
            guild=guild_id,
        )


if __name__ == "__main__":
    main()
