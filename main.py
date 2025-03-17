import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for name, player in players.items():
        player_race = Race.objects.get_or_create(
            name=player["race"]["name"],
            description=player["race"]["description"]
        )

        for skill in player["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=player_race[0]
            )

        try:
            player_guild = Guild.objects.get_or_create(
                name=player["guild"]["name"],
                description=player["guild"]["description"]
            )
        except TypeError:
            player_guild = [None]

        Player.objects.get_or_create(
            nickname=name,
            email=player["email"],
            bio=player["bio"],
            race=player_race[0],
            guild=player_guild[0]
        )


if __name__ == "__main__":
    main()
