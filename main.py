import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        all_info = json.load(f)

    for key, value in all_info.items():
        race_info = value["race"]
        if not Race.objects.filter(name=race_info["name"]).exists():
            race = Race.objects.create(name=race_info["name"],
                                       description=race_info["description"])
        else:
            race = Race.objects.get(name=race_info["name"])

        skills_info = race_info["skills"]
        for skill in skills_info:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"], bonus=skill["bonus"], race=race
                )

        guild_info = value["guild"]
        guild = None
        if guild_info:
            if not Guild.objects.filter(
                    name=guild_info["name"]).exists():
                guild = Guild.objects.create(
                    name=guild_info["name"],
                    description=guild_info["description"])
            else:
                guild = Guild.objects.get(name=guild_info["name"])

        if not Player.objects.filter(
                nickname=key).exists():
            Player.objects.create(nickname=key,
                                  email=value["email"], bio=value["bio"],
                                  race=race,
                                  guild=guild)


if __name__ == "__main__":
    main()
