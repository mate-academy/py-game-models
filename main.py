import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        file_json = json.load(f)
    for name, player_info in file_json.items():

        race = player_info.get("race")
        skills = player_info.get("race").get("skills")
        guild = player_info.get("guild")

        race = Race.objects.get_or_create(
            name=race.get("name"),
            description=race.get("description")
        )[0]

        for skill in skills:
            if not Skill.objects.filter(name=skill.get("name")).exists():
                Skill.objects.create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=race
                )

        if guild:
            guild = Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
            )[0]

        Player.objects.create(
            nickname=name,
            email=player_info.get("email"),
            bio=player_info.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
