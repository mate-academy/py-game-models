import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        players = json.load(f)
    for player in players:
        guild = players[player].get("guild")
        if guild is not None:
            if not Guild.objects.filter(
                    name=guild["name"]
            ).exists():
                Guild.objects.create(
                    name=guild["name"],
                    description=guild["description"]
                )
        race = players[player]["race"]
        if not Race.objects.filter(
                name=race["name"]
        ).exists():
            Race.objects.create(
                name=race["name"],
                description=race["description"]
            )
        skills = players[player]["race"]["skills"]
        for skill in skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(name=race["name"])
                )
        player_info = players[player]
        if not Player.objects.filter(nickname=player).exists():
            Player.objects.create(
                nickname=player,
                email=player_info["email"],
                bio=player_info["bio"],
                race=Race.objects.get(name=race["name"]),
                guild=Guild.objects.get(name=guild["name"])
                if guild is not None else None
            )


if __name__ == "__main__":
    main()
