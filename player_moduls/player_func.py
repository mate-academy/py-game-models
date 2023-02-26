from db.models import Player
from player_moduls.race_func import race_func
from player_moduls.guild_func import guild_func


def player_func(players: dict) -> None:
    for player_name, player in players.items():
        Player.objects.create(
                nickname=player_name,
                email=player["email"],
                bio=player["bio"],
                race=race_func(player),
                guild=guild_func(player),
            )
