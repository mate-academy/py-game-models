import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def create_race(race: dict) -> None:
    if not Race.objects.filter(name=race["name"]).exists():
        Race.objects.create(
            name=race["name"],
            description=race["description"]
        )


def get_race_by_name(race: dict) -> Race:
    return Race.objects.get(name=race["name"])


def create_skills(skills: list[dict], race: dict) -> None:
    for skill in skills:
        if not Skill.objects.filter(name=skill["name"]).exists():
            Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=get_race_by_name(race)
            )


def create_guild(guild: dict) -> None:
    if guild and not Guild.objects.filter(name=guild["name"]).exists():
        Guild.objects.create(
            name=guild["name"],
            description=guild["description"]
        )


def get_guild_by_name(guild: dict) -> Guild:
    return Guild.objects.get(name=guild["name"])


def main() -> None:
    with open("players.json") as data_file:
        data = json.load(data_file)

    for player in data:

        create_race(data[player]["race"])
        create_skills(skills=data[player]["race"]["skills"],
                      race=data[player]["race"])
        create_guild(guild=data[player]["guild"])

        if not Player.objects.filter(nickname=player).exists():
            Player.objects.create(
                nickname=player,
                email=data[player]["email"],
                bio=data[player]["bio"],
                race=get_race_by_name(race=data[player]["race"]),
                guild=get_guild_by_name(guild=data[player]["guild"])
                if data[player]["guild"] else None,
            )


if __name__ == "__main__":
    main()
