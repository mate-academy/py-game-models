import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main():
    players_data = get_player_data("players.json")

    for player_name, player_data in players_data.items():
        race = create_race(player_data["race"])

        create_skills(race, player_data["race"]["skills"])

        if player_data["guild"]:
            guild = create_guild(player_data["guild"])
        else:
            guild = None

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            guild=guild,
            race=race
        )


def create_race(race_data: dict) -> Race:
    race, _ = Race.objects.get_or_create(
        name=race_data["name"],
        description=race_data["description"]
    )

    return race


def create_skills(race: Race, skills_list: list):
    for skill in skills_list:
        if not Skill.objects.filter(name=skill["name"]).exists():
            Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )


def create_guild(guild_data: dict) -> Guild:
    guild, _ = Guild.objects.get_or_create(
        name=guild_data["name"],
        description=guild_data["description"]
    )

    return guild


def get_player_data(file_name: str) -> dict:
    with open(file_name) as file:
        players_data = json.load(file)

    return players_data


if __name__ == "__main__":
    main()
