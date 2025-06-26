import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def load_players_from_file(path: str) -> dict[str, dict]:
    with open(path) as file:
        return json.load(file)


def create_skills_for_race(race: Race, skills_data: list[dict]) -> None:
    for skill_data in skills_data:
        Skill.objects.get_or_create(
            name=skill_data["name"],
            bonus=skill_data["bonus"],
            race=race
        )


def get_or_create_race(race_data: dict) -> Race:
    race, _ = Race.objects.get_or_create(
        name=race_data["name"],
        defaults={"description": race_data.get("description", "")}
    )

    skills_data = race_data.get("skills", [])
    if skills_data:
        create_skills_for_race(race, skills_data)

    return race


def get_or_create_guild(guild_data: dict | None) -> Guild | None:
    if not guild_data:
        return None

    guild, _ = Guild.objects.get_or_create(
        name=guild_data["name"],
        defaults={"description": guild_data.get("description", "")}
    )
    return guild


def build_player_from_data(player_name: str, data: dict) -> Player:
    race = get_or_create_race(data["race"])
    guild = get_or_create_guild(data.get("guild"))

    return Player.objects.create(
        nickname=player_name,
        email=data["email"],
        bio=data["bio"],
        race=race,
        guild=guild
    )


def main() -> None:
    players = load_players_from_file("players.json")

    for player_name, player_data in players.items():
        build_player_from_data(player_name, player_data)


if __name__ == "__main__":
    main()
