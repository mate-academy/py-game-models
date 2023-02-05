import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as read_file:
        players = json.load(read_file)

    for player_name, info in players.items():
        if not Race.objects.filter(
                name=info["race"]["name"]).exists():
            Race.objects.create(
                name=info["race"]["name"],
                description=info["race"]["description"]
            )
        race = Race.objects.get(
            name=info["race"]["name"])

        if info["guild"] is not None:
            if not Guild.objects.filter(
                    name=info["guild"]["name"]).exists():
                guild = Guild.objects.create(
                    name=info["guild"]["name"],
                    description=info["guild"]["description"]
                )
            guild = Guild.objects.get(
                name=info["guild"]["name"])
        else:
            guild = None

        Player.objects.create(
            nickname=player_name,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild
        )
        skills = info["race"]["skills"] if info["race"]["skills"] else None
        if skills:
            for skill in skills:
                if not Skill.objects.filter(
                        name=skill["name"]).exists():
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race
                    )


if __name__ == "__main__":
    main()
