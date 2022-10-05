import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json", "r") as all_info:
        info_about_player = json.load(all_info)
    for nickname, player in info_about_player.items():
        if not Race.objects.filter(name=player["race"]["name"]).exists():
            Race.objects.create(
                name=player["race"]["name"],
                description=player["race"]["description"]
            )
        race = Race.objects.get(name=player["race"]["name"])
        for skill in player["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )
        guild = None
        if player["guild"]:
            if not Guild.objects.filter(name=player["guild"]["name"]). \
                    exists():
                Guild.objects.create(
                    name=player["guild"]["name"],
                    description=player["guild"]["description"]

                )
            guild = Guild.objects.get(name=player["guild"]["name"])
        Player.objects.create(
            nickname=nickname,
            email=player["email"],
            bio=player["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
