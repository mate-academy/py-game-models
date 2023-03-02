import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for race in data.values():
        name = race.get("race").get("name")
        description = race.get("race").get("description")
        if not Race.objects.filter(name=name).exists():
            Race.objects.create(name=name, description=description)
        skills_list = race.get("race").get("skills")
        if skills_list:
            for skill in skills_list:
                if not Skill.objects.filter(name=skill.get("name")).exists():
                    Skill.objects.create(
                        name=skill.get("name"),
                        bonus=skill.get("bonus"),
                        race=Race.objects.get(name=name)
                    )

    for guild in data.values():
        if not guild.get("guild"):
            continue
        name = guild.get("guild").get("name")
        description = guild.get("guild").get("description")
        if not Guild.objects.filter(name=name).exists():
            Guild.objects.create(name=name, description=description)

    for player, atr in data.items():
        race = Race.objects.filter(name=atr.get("race").get("name")).values("id")[0]["id"]
        try:
            guild = Guild.objects.filter(name=atr.get("guild").get("name")).values("id")[0]["id"]
        except AttributeError:
            guild = None

        Player.objects.create(
            nickname=player,
            email=atr.get("email"),
            bio=atr.get("bio"),
            race_id=race,
            guild_id=guild
        )

if __name__ == "__main__":
    main()
