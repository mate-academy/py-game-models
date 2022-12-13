import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:

    with open("players.json", "r") as f:
        user_data = json.load(f)
        for name, info in user_data.items():
            race = Race.objects
            guild = Guild.objects
            if not race.filter(name=info["race"]["name"]).exists():
                race.create(name=info["race"]["name"],
                            description=info["race"]["description"])
                for skill in info["race"]["skills"]:
                    if not Skill.objects.filter(name=skill["name"]).exists():
                        Skill.objects.create(name=skill["name"],
                                             bonus=skill["bonus"],
                                             race=Race.objects.get
                                             (name=info["race"]["name"]))

            if info["guild"] is not None:
                if not guild.filter(
                        name=info["guild"]["name"]).exists():
                    guild.create(
                        name=info["guild"]["name"],
                        description=info["guild"]["description"])
                guild = guild.get(name=info["guild"]["name"])
            else:
                guild = None

            if not Player.objects.filter(nickname=name).exists():
                Player.objects.create(nickname=name,
                                      email=info["email"],
                                      bio=info["bio"],
                                      race=Race.objects.get
                                      (name=info["race"]["name"]),
                                      guild=guild)


if __name__ == "__main__":
    main()
