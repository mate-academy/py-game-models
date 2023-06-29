import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def create_race(race_info: dict) -> None:
    if not Race.objects.filter(name=race_info["name"]).exists():
        Race.objects.create(
            name=race_info["name"],
            description=race_info["description"]
        )


def get_race_id(race_info: dict) -> int:
    return Race.objects.get(name=race_info["name"]).id


def create_skills(race_info: dict) -> None:
    skills_list = race_info["skills"]
    if skills_list:
        for skill in skills_list:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race_id=get_race_id(race_info)
                )


def create_guild(guild_info: dict) -> None:
    if guild_info and not Guild.objects.filter(
            name=guild_info["name"]
    ).exists():
        Guild.objects.create(
            name=guild_info["name"],
            description=guild_info["description"]
        )


def get_guild_id(guild_info: dict) -> int | None:
    return (Guild.objects.get(name=guild_info["name"]).id
            if guild_info
            else None)


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player in players:
        create_race(players[player]["race"])
        create_skills(players[player]["race"])
        create_guild(players[player]["guild"])
        race_id = get_race_id(players[player]["race"])
        guild_id = get_guild_id(players[player]["guild"])

        Player.objects.create(
            nickname=player,
            email=players[player]["email"],
            bio=players[player]["bio"],
            race_id=race_id,
            guild_id=guild_id
        )


if __name__ == "__main__":
    main()
