import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as dict_players:
        players = json.load(dict_players)

    for nick in players:
        player = players[nick]
        skills = player["race"]["skills"]
        race = player["race"]
        guild = player["guild"] if player["guild"] else None

        if not Race.objects.filter(name=race["name"]).exists():
            Race.objects.create(
                name=race["name"],
                description=race["description"]
            )
        race = Race.objects.get(name=race["name"])

        if guild:
            if not Guild.objects.filter(name=guild["name"]).exists():
                Guild.objects.create(
                    name=guild["name"],
                    description=guild["description"]
                )
            guild = Guild.objects.get(name=guild["name"])

        for item in skills:
            if not Skill.objects.filter(name=item["name"]).exists():
                Skill.objects.create(
                    name=item["name"],
                    bonus=item["bonus"],
                    race=race
                )

        Player.objects.create(
            nickname=nick,
            email=player["email"],
            bio=player["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
