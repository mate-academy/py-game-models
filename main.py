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

        if Race.objects.filter(name=race.get("name")).exists():
            race = Race.objects.get(name=race.get("name"))
        else:
            race = Race.objects.create(
                name=race.get("name"),
                description=race.get("description")
            )

        for skill in skills:
            if not Skill.objects.filter(name=skill.get("name")).exists():
                Skill.objects.create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=race
                )

        if guild:
            if Guild.objects.filter(name=guild.get("name")).exists():
                guild = Guild.objects.get(name=guild.get("name"))
            else:
                guild = Guild(
                    name=guild.get("name"),
                    description=guild.get("description")
                )
                guild.save()

        Player.objects.create(
            nickname=name,
            email=player_info.get("email"),
            bio=player_info.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
