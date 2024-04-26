import json

import init_django_orm  # noqa: F401

from db.models import Race, Player, Guild


def create_race(player_data: dict) -> Race:
    race_name = player_data["race"]["name"]
    race_description = player_data["race"]["description"]
    race, _ = Race.objects.get_or_create(
        name=race_name,
        description=race_description
    )
    return race


def create_guild(player_data: dict) -> Guild | None:
    guild_data = player_data.get("guild")
    if guild_data:
        guild_name = guild_data["name"]
        guild_description = guild_data["description"]
        guild, _ = Guild.objects.get_or_create(
            name=guild_name,
            description=guild_description
        )
        return guild
    return None


def create_player(
        player_name: str,
        player_data: dict,
        race: Race,
        guild: Guild
) -> Player:
    email = player_data["email"]
    bio = player_data["bio"]
    player = Player.objects.create(
        nickname=player_name,
        email=email,
        bio=bio, race=race, guild=guild
    )
    return player


def create_skills(player: Player, player_data: dict) -> None:
    for skill in player_data["race"]["skills"]:
        name = skill["name"]
        bonus = skill["bonus"]
        player.race.skill_set.get_or_create(name=name, bonus=bonus)


def main() -> None:
    with open("players.json", "r") as json_file:
        players_data = json.load(json_file)

    for player_name, player_info in players_data.items():
        try:
            player_race = create_race(player_info)
            player_guild = create_guild(player_info)
            player = create_player(player_name, player_info,
                                   player_race, player_guild)
            create_skills(player, player_info)
        except Exception as error:
            print(f"Error creating player {player_name}: {str(error)}")


if __name__ == "__main__":
    main()
