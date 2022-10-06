import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json") as file_in:
        data = json.load(file_in)

    for name, info in data.items():
        guild = None
        if info["guild"] is not None:
            guild, created = Guild.objects.get_or_create(**info["guild"])
        race, created = Race.objects.get_or_create(name=info["race"]["name"],
                                                   description=info["race"]
                                                   ["description"]
                                                   )
        if info["race"]["skills"]:
            for skill in info["race"]["skills"]:
                Skill.objects.get_or_create(race=race, **skill)

        Player.objects.create(
            nickname=name,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
