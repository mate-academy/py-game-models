import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def load_players_data(filename: str) -> dict:
    with open(filename, "r") as file:
        return json.load(file)


def get_or_create_race(race_data: dict) -> Race:
    race, _ = Race.objects.get_or_create(
        name=race_data["name"],
        defaults={"description": race_data.get("description", "")}
    )

    for skill_data in race_data.get("skills", []):
        Skill.objects.get_or_create(
            name=skill_data["name"],
            defaults={"bonus": skill_data["bonus"], "race": race}
        )

    return race


def get_or_create_guild(guild_data: dict | None) -> Guild | None:
    if not guild_data:
        return None

    guild, _ = Guild.objects.get_or_create(
        name=guild_data["name"],
        defaults={"description": guild_data.get("description", "")}
    )
    return guild


def create_player(player_name: str, player_data: dict) -> None:
    race = get_or_create_race(player_data["race"])
    guild = get_or_create_guild(player_data.get("guild"))

    Player.objects.get_or_create(
        nickname=player_name,
        defaults={
            "email": player_data["email"],
            "bio": player_data["bio"],
            "race": race,
            "guild": guild,
        }
    )


def main() -> None:
    players_data = load_players_data("players.json")

    for player_name, player_data in players_data.items():
        create_player(player_name, player_data)


if __name__ == "__main__":
    main()
