import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def load_players_data() -> dict:
    with open("players.json", "r") as file:
        return json.load(file)


def get_or_create_race(race_data: dict) -> Race:
    return Race.objects.get_or_create(
        name=race_data["name"],
        defaults={"description": race_data.get("description", "")}
    )[0]


def create_skills_for_race(race: Race, skills_data: list) -> None:
    for skill_data in skills_data:
        Skill.objects.get_or_create(
            name=skill_data["name"],
            defaults={"bonus": skill_data["bonus"], "race": race}
        )


def get_or_create_guild(guild_data: dict) -> Guild:
    if guild_data:
        return Guild.objects.get_or_create(
            name=guild_data["name"],
            defaults={"description": guild_data.get("description", "")}
        )[0]
    return None


def create_player(player_name: str,
                  player_data: dict,
                  race: Race,
                  guild: Guild) -> None:
    Player.objects.get_or_create(
        nickname=player_name,
        defaults={
            "email": player_data["email"],
            "bio": player_data["bio"],
            "race": race,
            "guild": guild
        }
    )


def main() -> None:
    pass
    players_data = load_players_data()

    for player_name, player_data in players_data.items():
        race_data = player_data["race"]
        race = get_or_create_race(race_data)
        create_skills_for_race(race, race_data["skills"])

        guild_data = player_data.get("guild")
        guild = get_or_create_guild(guild_data)

        create_player(player_name, player_data, race, guild)


if __name__ == "__main__":
    main()
