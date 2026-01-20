import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def create_guild(guild_info: None | dict) -> Guild | None:
    if guild_info:
        guild_name = guild_info["name"]
        if not Guild.objects.filter(name=guild_name).exists():
            return Guild.objects.create(
                name=guild_name,
                description=guild_info["description"]
            )
        return Guild.objects.get(name=guild_name)
    return None


def create_race(race_info: dict) -> Race:
    race_name = race_info["name"]
    if not Race.objects.filter(name=race_name).exists():
        return Race.objects.create(
            name=race_info["name"],
            description=race_info["description"]
        )
    return Race.objects.get(name=race_name)


def create_skills(skills: list[dict], race: Race) -> None:
    for skill in skills:
        if not Skill.objects.filter(name=skill["name"]).exists():
            Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )


def store_information_into_db(filename: str) -> None:
    with open(filename, "r") as f:
        data = json.load(f)

    for name, player_info in data.items():
        guild = create_guild(player_info["guild"])
        race = create_race(player_info["race"])
        create_skills(player_info["race"]["skills"], race)

        Player.objects.create(
            nickname=name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild,
        )


def main() -> None:
    store_information_into_db("players.json")


if __name__ == "__main__":
    main()
