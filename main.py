from json import load

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = load(file)
    for player, data in data.items():
        race = data.get("race")
        skills = data.get("race").get("skills")
        guild = data.get("guild")

        if Race.objects.filter(name=race.get("name")).exists():
            race = Race.objects.get(name=race.get("name"))
        else:
            race = Race(
                name=race.get("name"),
                description=race.get("description")
            )
            race.save()

        for skill in skills:
            if not Skill.objects.filter(name=skill.get("name")).exists():
                skill = Skill(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=race
                )
                skill.save()

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
            nickname=player,
            email=data.get("email"),
            bio=data.get("bio"),
            race=race,
            guild=guild
        )
        player.save()


if __name__ == "__main__":
    main()
