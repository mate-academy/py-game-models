def get_race_data(players: dict) -> dict:
    race_data = dict()
    for player in players:
        race_data.update(
            {
                players[player]["race"]["name"]:
                    players[player]["race"]["description"]
            }
        )
    return race_data
