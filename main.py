import init_django_orm  # noqa: F401
import json

from db.models import Guild, Player, Skill, Race


def main() -> None:
    with open("players.json", "r") as file_in:
        players = json.load(file_in)

    for player, data in players.items():
        race = data["race"]["name"]
        guild = data["guild"] or None
        skills = data["race"]["skills"]

        if not Race.objects.filter(name=race).exists():
            Race.objects.create(
                name=race,
                description=data["race"]["description"]
            )

        for skill_info in skills:
            if not Skill.objects.filter(name=skill_info["name"]).exists():
                Skill.objects.create(
                    name=skill_info["name"],
                    bonus=skill_info["bonus"],
                    race=Race.objects.get(name=race)
                )

        if guild:
            if not Guild.objects.filter(name=guild["name"]).exists():
                Guild.objects.create(
                    name=guild["name"],
                    description=guild["description"]
                )

        if not Player.objects.filter(nickname=player).exists():
            Player.objects.create(
                nickname=player,
                email=data["email"],
                bio=data["bio"],
                race=Race.objects.get(name=race),
                guild=Guild.objects.get(name=guild["name"])
                if guild else None)


if __name__ == "__main__":
    main()
