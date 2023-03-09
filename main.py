import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for name, info in data.items():
        race = info.get("race")
        skills = info.get("race").get("skills")
        guild = info.get("guild")

        # For class Race
        if Race.objects.filter(name=race.get("name")).exists():
            new_race = Race.objects.get(name=race.get("name"))
        else:
            new_race = Race(
                name=race.get("name"),
                description=race.get("description")
            )
            new_race.save()

        # For class Skill
        for skill in skills:
            if not Skill.objects.filter(name=skill.get("name")).exists():
                new_skill = Skill(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=new_race
                )
                new_skill.save()

        # For class Guild
        if guild:
            if Guild.objects.filter(name=guild.get("name")).exists():
                guild = Guild.objects.get(name=guild.get("name"))
            else:
                guild = Guild(
                    name=guild.get("name"),
                    description=guild.get("description")
                )
                guild.save()

        player = Player(
            nickname=name,
            email=info.get("email"),
            bio=info.get("bio"),
            race=new_race,
            guild=guild
        )
        player.save()


if __name__ == "__main__":
    main()
