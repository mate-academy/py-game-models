import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild
import json


def create_race(info: dict) -> Race :
    if not Race.objects.filter(name=info["race"]["name"]).exists():
        race = Race.objects.create(
            name=info["race"]["name"],
            description=info["race"]["description"]
        )
        skills = info["race"]["skills"]
        if skills:
            for skill in skills:
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )
    return Race.objects.get(name=info["race"]["name"])


def create_guild(info: dict) -> Guild:
    guild = None
    if info["guild"]:
        if not Guild.objects.filter(name=info["guild"]["name"]).exists():
            guild = Guild.objects.create(
                name=info["guild"]["name"],
                description=info["guild"]["description"],
            )
        else:
            guild = Guild.objects.get(name=info["guild"]["name"])
    return guild


def create_player(player: str, info: dict) -> Player:
    race = create_race(info)
    guild = create_guild(info)

    Player.objects.create(
        nickname=player,
        email=info["email"],
        bio=info["bio"],
        race=race,
        guild=guild
    )


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player, info in players.items():
        create_player(player, info)


if __name__ == "__main__":
    main()
