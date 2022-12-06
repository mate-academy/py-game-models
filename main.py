import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_dict = json.load(file)

    for player, info in players_dict.items():

        if not Race.objects.filter(name=info["race"]["name"]).exists():
            race_of_player = Race.objects.create(
                name=info["race"]["name"],
                description=info["race"]["description"]
            )

            for skill in info["race"]["skills"]:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race_of_player
                    )
        else:
            race_of_player = Race.objects.get(name=info["race"]["name"])

        guild = None
        if info["guild"] is not None:
            if not Guild.objects.filter(name=info["guild"]["name"]).exists():
                guild = Guild.objects.create(
                    name=info["guild"]["name"],
                    description=info["guild"]["description"]
                )
        else:
            guild = Guild.objects.get(
                name=info["guild"]["name"]
            )

        Player.objects.create(
            nickname=player,
            email=info["email"],
            bio=info["bio"],
            race=race_of_player,
            guild=guild
        )


if __name__ == "__main__":
    main()
