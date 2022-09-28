import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json") as file:
        players = json.load(file)

        for key, value in players.items():
            if not Race.objects.filter(name=value["race"]["name"]).exists():
                Race.objects.create(
                    name=value["race"]["name"],
                    description=value["race"]["description"]
                )
            race = Race.objects.get(name=value["race"]["name"])
            for skill in value["race"]["skills"]:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race
                    )
            guild = None
            if value["guild"]:
                if not Guild.objects.filter(name=value["guild"]["name"]).\
                        exists():
                    Guild.objects.create(
                        name=value["guild"]["name"],
                        description=value["guild"]["description"]
                        if value["guild"]["description"] is not None else None
                    )
                guild = Guild.objects.get(name=value["guild"]["name"])
            Player.objects.create(
                nickname=key,
                email=value["email"],
                bio=value["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
