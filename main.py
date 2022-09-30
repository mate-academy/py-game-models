import init_django_orm  # noqa: F401
import django
from db.models import Race, Skill, Player, Guild
import json


def main():
    with open("players.json") as file:
        content = json.load(file)

    for name_player, info in content.items():
        try:
            race = Race.objects.create(
                name=info["race"]["name"],
                description=info["race"]["description"]
            )
        except django.db.utils.IntegrityError:
            race = Race.objects.get(name=info["race"]["name"])

        for title, val in info["race"].items():
            if title == "skills":
                for item in val:
                    try:
                        Skill.objects.create(
                            name=item["name"],
                            bonus=item["bonus"],
                            race_id=race.id
                        )
                    except django.db.utils.IntegrityError:
                        continue
        try:
            guild = Guild.objects.create(
                name=info["guild"]["name"],
                description=info["guild"]["description"]
            )
        except TypeError:
            continue
        try:
            Player.objects.create(
                nickname=name_player,
                email=info["email"],
                bio=info["bio"],
                race_id=race.id,
                guild_id=guild.id
            )
        except django.db.utils.IntegrityError:
            continue


if __name__ == "__main__":
    main()
