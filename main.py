import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def create_race(race: dict) -> None:
    if not Race.objects.filter(name=race["name"]).exists():
        Race.objects.create(
            name=race["name"],
            description=race["description"]
        )


def get_race_id(race: dict) -> int:
    return Race.objects.get(name=race["name"])


def create_skills(skills: list[dict], race: dict) -> None:
    for skill in skills:
        if not Skill.objects.filter(name=skill["name"]).exists():
            Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=get_race_id(race)
            )


def create_guild(guild: dict) -> None:
    if guild and not Guild.objects.filter(name=guild["name"]).exists():
        Guild.objects.create(
            name=guild["name"],
            description=guild["description"]
        )


def get_guild_id(guild: dict) -> int:
    return Guild.objects.get(name=guild["name"])


def main() -> None:
    with open("players.json") as data_file:
        data = json.load(data_file)

    for player in data:
        player_data = data[player]
        race = player_data["race"]
        skills = race["skills"]
        guild = player_data["guild"]

        create_race(race)
        create_skills(skills, race)
        create_guild(guild)

        if not Player.objects.filter(nickname=player).exists():
            Player.objects.create(
                nickname=player,
                email=player_data["email"],
                bio=player_data["bio"],
                race=get_race_id(race),
                guild=get_guild_id(guild) if guild else None,
            )


if __name__ == "__main__":
    main()
