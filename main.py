import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for player in players:
        race, created = Race.objects.get_or_create(
            name=players[player]["race"]["name"],
            description=players[player]["race"]["description"])
        for skill in players[player]["race"]["skills"]:
            Skill.objects.get_or_create(name=skill["name"],
                                        bonus=skill["bonus"],
                                        race=race)
        if players[player]["guild"]:
            guild, created = Guild.objects.get_or_create(
                name=players[player]["guild"]["name"],
                description=players[player]["guild"]["description"])
        else:
            guild = players[player]["guild"]
        Player.objects.get_or_create(
            nickname=player,
            email=players[player]["email"],
            bio=players[player]["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
