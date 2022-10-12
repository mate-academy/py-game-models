import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file_in:
        data = json.load(file_in)
    for player, info in data.items():
        for key, value in info.items():
            if key == "race":
                if not Race.objects.filter(name=value["name"]).exists():
                    Race.objects.create(
                        name=value["name"],
                        description=value["description"],
                    )
                if value["skills"] is not None:
                    for skill in value["skills"]:
                        check_skill = Skill.objects.filter(
                            name=skill["name"]).exists()
                        if not check_skill:
                            Skill.objects.create(name=skill["name"],
                                                 bonus=skill["bonus"])
            if key == "guild" and value is not None:
                if not Guild.objects.filter(name=value["name"]).exists():
                    if value["description"] is None:
                        Guild.objects.create(
                            name=value["name"],
                            description=None,
                        )
                        continue
                    Guild.objects.create(
                        name=value["name"],
                        description=value["description"],
                    )
    for name, player in data.items():
        if player["guild"] is None:
            Player.objects.create(
                nickname=name,
                email=player["email"],
                bio=player["bio"],
                race_id=Race.objects.get(name=player["race"]["name"]).id,
                guild_id=None,
            )
        else:
            Player.objects.create(
                nickname=name,
                email=player["email"],
                bio=player["bio"],
                race_id=Race.objects.get(name=player["race"]["name"]).id,
                guild_id=Guild.objects.get(name=player["guild"]["name"]).id,
            )


if __name__ == "__main__":
    main()
