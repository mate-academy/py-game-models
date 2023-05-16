import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, info in data.items():
        race_info = info.get("race")
        race, _ = Race.objects.get_or_create(
            name=race_info.get("name"),
            description=race_info.get("description")
        )

        skills_info = race_info.get("skills")
        for skill_info in skills_info:
            skill, _ = Skill.objects.get_or_create(
                name=skill_info.get("name"),
                bonus=skill_info.get("bonus"),
                race=Race.objects.filter(name=race_info.get("name")).get()
            )
        if info.get("guild"):
            guild_info = info.get("guild")
            guild, _ = Guild.objects.get_or_create(
                name=guild_info.get("name"),
                description=guild_info.get("description")
            )
        else:
            guild = None

        Player.objects.create(
            nickname=nickname,
            email=info.get("email"),
            bio=info.get("bio"),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
