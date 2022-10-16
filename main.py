import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file_in:
        data = json.load(file_in)
    for player, info in data.items():
        if not Race.objects.filter(name=info["race"]["name"]).exists():
            Race.objects.create(
                name=info["race"]["name"],
                description=info["race"]["description"],
            )
        if info["race"]["skills"] is not None:
            for skill in info["race"]["skills"]:
                check_skill = Skill.objects.filter(
                    name=skill["name"]).exists()
                if not check_skill:
                    Skill.objects.create(name=skill["name"],
                                         bonus=skill["bonus"])
        if info["guild"] is not None:
            if not Guild.objects.filter(name=info["guild"]["name"]).exists():
                if info["guild"]["description"] is None:
                    Guild.objects.create(
                        name=info["guild"]["name"],
                        description=None,
                    )
                    continue
                Guild.objects.create(
                    name=info["guild"]["name"],
                    description=info["guild"]["description"],
                )
    for name, player in data.items():
        Player.objects.create(
            nickname=name,
            email=player["email"],
            bio=player["bio"],
            race_id=Race.objects.get(name=player["race"]["name"]).id,
            guild_id=None,
        ) if player["guild"] is None else Player.objects.create(
            nickname=name,
            email=player["email"],
            bio=player["bio"],
            race_id=Race.objects.get(name=player["race"]["name"]).id,
            guild_id=Guild.objects.get(name=player["guild"]["name"]).id,
        )


if __name__ == "__main__":
    main()
