import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def read_from_json(filename: str) -> dict:
    with open(filename, "r") as file:
        return json.load(file)


def create_skills(data: dict, player_race_id: int) -> None:
    for skill in data["skills"]:
        if not Skill.objects.filter(name=skill["name"]).exists():
            Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race_id=player_race_id
            )


def create_players(players: dict) -> None:

    for name, player_info in players.items():
        email, bio, race, guild = player_info.values()

        player_race_id = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )[0].id

        create_skills(race, player_race_id)

        if guild:
            player_guild_id = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )[0].id
        else:
            player_guild_id = None

        if not Player.objects.filter(nickname=name).exists():
            Player.objects.create(
                nickname=name,
                email=email,
                bio=bio,
                race_id=player_race_id,
                guild_id=player_guild_id
            )


def main() -> None:
    players = read_from_json("players.json")
    create_players(players)


if __name__ == "__main__":
    main()
