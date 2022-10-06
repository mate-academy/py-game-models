import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for name, data in players.items():

        race = create_race(data["race"])
        create_skill_from_list(data["race"]["skills"], race)

        guild = None
        if data["guild"] is not None:
            guild = create_guild(data["guild"])

        create_player(
            name,
            data,
            race,
            guild
        )


def create_player(
        player_name: str,
        player: dict,
        race: int,
        guild: int,
) -> None:
    if len(Player.objects.filter(nickname=player_name)) == 0:
        Player.objects.create(
            nickname=player_name,
            email=player["email"],
            bio=player["bio"],
            race_id=race,
            guild_id=guild
        )


def create_guild(guild: dict) -> int:
    if len(Guild.objects.filter(name=guild["name"])) == 0:
        Guild.objects.create(
            name=guild["name"],
            description=guild["description"]
        )

    return Guild.objects.get(name=guild["name"]).id


def create_race(race: dict) -> int:
    if len(Race.objects.filter(name=race["name"])) == 0:
        Race.objects.create(
            name=race["name"],
            description=race["description"]
        )

    return Race.objects.get(name=race["name"]).id


def create_skill_from_list(skills: list, race: int) -> None:
    for skill in skills:
        if len(Skill.objects.filter(name=skill["name"])) == 0:
            Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race_id=race
            )


if __name__ == "__main__":
    main()
