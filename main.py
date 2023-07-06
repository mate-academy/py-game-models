import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def create_guild(guild: dict) -> None:
    if guild:
        Guild.objects.get_or_create(
            name=guild["name"],
            description=guild["description"]
        )


def get_guild_id(guild: dict) -> int | None:
    return Guild.objects.get(name=guild["name"]).id if guild else None


def create_race(race: dict) -> None:
    Race.objects.get_or_create(
        name=race["name"],
        description=race["description"]
    )


def get_race_id(race_name: dict) -> int:
    return Race.objects.get(name=race_name).id


def create_skills(race: dict) -> None:
    for skill in race["skills"]:
        if not Skill.objects.filter(name=skill["name"]).exists():
            Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race_id=get_race_id(race["name"])
            )


def create_players() -> None:
    with open("players.json", "r") as players:
        players = json.load(players)
    for player, info in players.items():
        create_guild(info["guild"])
        create_race(info["race"])
        create_skills(info["race"])

        guild_id = get_guild_id(info["guild"])
        race_id = get_race_id(info["race"]["name"])

        Player.objects.create(
            nickname=player,
            email=info["email"],
            bio=info["bio"],
            guild_id=guild_id,
            race_id=race_id
        )


def main() -> None:
    create_players()


if __name__ == "__main__":
    main()
