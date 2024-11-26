import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def race(info: dict) -> Race:
    return Race.objects.get_or_create(
        name=info["race"]["name"],
        description=info["race"]["description"]
    )[0]


def skill(info: dict, race_choose: Race) -> None:
    for el in info["race"]["skills"]:
        Skill.objects.get_or_create(
            name=el["name"],
            bonus=el["bonus"],
            race=race_choose
        )


def guild(info: dict) -> Guild | None:
    if info["guild"]:
        return Guild.objects.get_or_create(
            name=info["guild"]["name"],
            description=info["guild"]["description"]
        )[0]
    return None


def player(name: str, info: dict, race_choose: Race, if_guild: Guild) -> None:
    Player.objects.create(
        nickname=name,
        email=info["email"],
        bio=info["bio"],
        race=race_choose,
        guild=if_guild
    )


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player_name, info in data.items():
        race_chosen = race(info)
        skill(info, race_chosen)
        is_guild = guild(info)
        player(player_name, info, race_chosen, is_guild)


if __name__ == "__main__":
    main()
