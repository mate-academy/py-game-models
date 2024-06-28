import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player in players:
        race = Race.objects.get_or_create(
            name=players[player]["race"]["name"],
            description=players[player]["race"]["description"],
        )

        for skill in players[player]["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race[0],
            )

        if players[player]["guild"] is not None:
            guild = Guild.objects.get_or_create(
                name=players[player]["guild"]["name"],
                description=players[player]["guild"]["description"],
            )
        else:
            guild = (None,)

        Player.objects.get_or_create(
            nickname=player,
            email=players[player]["email"],
            bio=players[player]["bio"],
            race=race[0],
            guild=guild[0],
        )


if __name__ == "__main__":
    main()
