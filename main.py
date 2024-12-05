import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as json_file:
        players = json.load(json_file)

    for key, player in players.items():
        if player["race"]["skills"]:
            for skill in player["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get_or_create(
                        name=player["race"]["name"],
                        description=player["race"]["description"],
                    )[0],
                )

    for key, player in players.items():

        Player.objects.get_or_create(
            nickname=key,
            email=player["email"] if player["email"] else None,
            bio=player["bio"] if player["bio"] else None,
            race=Race.objects.get_or_create(
                name=player["race"]["name"],
                description=player["race"]["description"],
            )[0],
            guild=(
                Guild.objects.get_or_create(
                    name=player["guild"]["name"],
                    description=(
                        player["guild"]["description"]
                        if player["guild"]["description"]
                        else None
                    ),
                )[0]
                if player["guild"]
                else None
            ),
        )


if __name__ == "__main__":
    main()
