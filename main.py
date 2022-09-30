import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json", "r") as all_info:
        info_about_player = json.load(all_info)
    for key, value in info_about_player.items():
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
            if not Guild.objects.filter(name=value["guild"]["name"]). \
                    exists():
                Guild.objects.create(
                    name=value["guild"]["name"],
                    description=value["guild"]["description"]

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
