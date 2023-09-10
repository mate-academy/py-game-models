import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players_data = json.load(f)

    for nickname, data in players_data.items():
        if not Race.objects.filter(name=data["race"]["name"]).exists():
            race = Race.objects.create(
                name=data["race"]["name"],
                description=data["race"]["description"]
            )

        for skill in data["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        if data["guild"]:
            if not Guild.objects.filter(name=data["guild"]["name"]).exists():
                guild = Guild.objects.create(
                    name=data["guild"]["name"],
                    description=data["guild"]["description"]
                )
        else:
            guild = None

        if not Player.objects.filter(nickname=nickname).exists():
            Player.objects.create(
                nickname=nickname,
                email=data["email"],
                bio=data["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
