import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file_in:
        players_data = json.load(file_in)

    for player, data in players_data.items():

        if not Race.objects.filter(name=data["race"]["name"]).exists():
            Race.objects.create(
                name=data["race"]["name"],
                description=data["race"]["description"]
            )

        for skill_info in data["race"]["skills"]:
            if not Skill.objects.filter(name=skill_info["name"]).exists():
                Skill.objects.create(
                    name=skill_info["name"],
                    bonus=skill_info["bonus"],
                    race=Race.objects.get(name=data["race"]["name"])
                )

        if data["guild"]:
            if not Guild.objects.filter(name=data["guild"]["name"]).exists():
                Guild.objects.create(
                    name=data["guild"]["name"],
                    description=data["guild"]["description"]
                )

        if not Player.objects.filter(nickname=player).exists():
            Player.objects.create(
                nickname=player,
                email=data["email"],
                bio=data["bio"],
                race=Race.objects.get(name=data["race"]["name"]),
                guild=Guild.objects.get(name=data["guild"]["name"])
                if data["guild"] else None)


if __name__ == "__main__":
    main()
