import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_info:
        data = json.load(players_info)

    for player, info in data.items():

        current_guild = None

        if Race.objects.filter(name=info["race"]["name"]).exists():
            current_race = Race.objects.get(
                name=info["race"]["name"])
        else:
            current_race = Race.objects.create(
                name=info["race"]["name"],
                description=info["race"]["description"])

        if info["guild"]:
            if Guild.objects.filter(name=info["guild"]["name"]).exists():
                current_guild = Guild.objects.get(name=info["guild"]["name"])
            else:
                current_guild = Guild.objects.create(
                    name=info["guild"]["name"],
                    description=info["guild"]["description"])

        for skill in info["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=current_race
                )
        Player.objects.create(
            nickname=player,
            email=info["email"],
            bio=info["bio"],
            race=current_race,
            guild=current_guild,
        )


if __name__ == "__main__":
    main()
