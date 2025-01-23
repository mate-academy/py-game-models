import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Guild.objects.all().delete()
    Player.objects.all().delete()

    with open("players.json", "r") as f:
        data = json.load(f)

    players = data
    for player in players:
        race, created = Race.objects.get_or_create(
            name=players[player]["race"]["name"],
            description=players[player]["race"]["description"]
        )
        for skill in range(len(players[player]["race"]["skills"])):
            skills, created = Skill.objects.get_or_create(
                name=players[player]["race"]["skills"][skill]["name"],
                bonus=players[player]["race"]["skills"][skill]["bonus"],
                race=race
            )
        if players[player].get("guild"):
            guild, created = Guild.objects.get_or_create(
                name=players[player]["guild"]["name"],
                description=players[player]["guild"]["description"]
            )

        Player.objects.create(
            nickname=player,
            email=players[player]["email"],
            bio=players[player]["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
