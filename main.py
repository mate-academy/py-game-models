import init_django_orm  # noqa: F401
import json

from typing import Dict

from db.models import Race, Skill, Player, Guild


def reader(filename: str) -> Dict:
    with open(filename) as file:
        return json.load(file)


def create_or_update_race(players_race: dict) -> Race:
    race, _ = Race.objects.get_or_create(
        name=players_race["name"],
        defaults={"description": players_race["description"]}
    )
    return race


def create_or_update_skills(players_race: dict, race_instance: Race) -> None:
    for skill in players_race:
        skill_instance, _ = Skill.objects.get_or_create(
            name=skill["name"],
            bonus=skill["bonus"],
            race=race_instance
        )


def create_or_update_guild(player_guild: dict) -> Guild | None:
    if player_guild:
        guild, _ = Guild.objects.get_or_create(
            name=player_guild["name"],
            defaults={"description": player_guild["description"]}
        )
        return guild
    return None


def create_player(
        player_name: str,
        player_data: dict,
        race: Race,
        guild: Guild
) -> None:
    Player.objects.create(
        nickname=player_name,
        email=player_data["email"],
        bio=player_data["bio"],
        race=race,
        guild=guild,
    )


def main() -> None:
    data = reader("players.json")

    for player_name, player_data in data.items():
        race_data = player_data["race"]
        guild_data = player_data["guild"]

        race = create_or_update_race(race_data)
        create_or_update_skills(race_data["skills"], race)
        guild = create_or_update_guild(guild_data)

        create_player(player_name, player_data, race, guild)

if __name__ == "__main__":
    main()
