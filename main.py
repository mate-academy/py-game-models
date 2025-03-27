import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        player_info = json.load(f)

    for player_name, info in player_info.items():
        if not Race.objects.filter(name=info["race"]["name"]).exists():
            Race.objects.create(
                name=info["race"]["name"],
                description=info["race"]["description"]
            )
        race = Race.objects.get(name=info["race"]["name"])

        for skill in info["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        if info["guild"]:
            if not Guild.objects.filter(name=info["guild"]["name"]).exists():
                Guild.objects.create(
                    name=info["guild"]["name"],
                    description=info["guild"]["description"]
                )
            guild = Guild.objects.get(name=info["guild"]["name"])
        else:
            guild = None

        if not Player.objects.filter(nickname=player_name).exists():
            Player.objects.create(
                nickname=player_name,
                email=info["email"],
                bio=info["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
