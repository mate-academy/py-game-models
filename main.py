import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player in players:
        race, _ = Race.objects.get_or_create(
            name=players[player]["race"]["name"],
            description=players[player]["race"]["description"],
        )

        for skill in players[player]["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race,
            )

        guild = None
        if players[player]["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=players[player]["guild"]["name"],
                description=players[player]["guild"]["description"],
            )

        Player.objects.get_or_create(
            nickname=player,
            email=players[player]["email"],
            bio=players[player]["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
