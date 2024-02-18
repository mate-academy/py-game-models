from datetime import datetime

from data_from_players.get_player_data import get_player_data

from db.models import Player
from players_json import players_data


def create_player() -> Player:
    player_lst = get_player_data(players_data)
    for player in player_lst:
        print(player)
        Player.objects.get_or_create(
            nickname=player[0],
            email=player[1],
            bio=player[2],
            race=player[3],
            guild=player[4],
            created_at=datetime.now(),
        )
    return Player.objects
